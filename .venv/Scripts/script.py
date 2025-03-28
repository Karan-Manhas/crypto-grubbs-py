import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
import os
from datetime import datetime

# MySQL connection details (replace with your own)
DB_USER = "####"
DB_PASSWORD = "####"
DB_NAME = "####"
DB_URL = "####"
DB_PORT = '####'

# table name for dynamic naming ( found in C:\Users\Karan\repos\CryptoGrubbsPy\.venv\kyber_benchmark_1000) )
TABLE_NAME = "kyber_benchmark_1000"

def connect_to_db():
    return mysql.connector.connect(
        host=DB_URL, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT
    )

def fetch_data():
    query = f"""
    SELECT crypto_operation, iteration_no, time_ns
    FROM {TABLE_NAME};
    """
    conn = connect_to_db()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# compute grubbs' test statis
def grubbs_test(df, column="time_ns"):
    mean = df[column].mean()
    std_dev = df[column].std()

    # min and max  extreme value
    max_outlier = df.loc[df[column].idxmax()]
    min_outlier = df.loc[df[column].idxmin()]

    # compute Grubbs' test statis
    G_max = abs(max_outlier[column] - mean) / std_dev
    G_min = abs(min_outlier[column] - mean) / std_dev

    #  critical value
    N = len(df)
    t_value = t.ppf(1 - 0.05 / (2 * N), N - 2)
    G_critical = ((N - 1) / (N ** 0.5)) * ((t_value ** 2 / (N - 2 + t_value ** 2)) ** 0.5)

    # remove entire iteration if either process is an outlier
    if G_max > G_critical:
        return df[df["iteration_no"] != max_outlier["iteration_no"]]
    elif G_min > G_critical:
        return df[df["iteration_no"] != min_outlier["iteration_no"]]
    else:
        return df

# iteratively apply grubbs' test until no more outliers
def remove_outliers(df):
    df_filtered = df.copy()
    sd_trend = []  

    while True:
        prev_std = df_filtered["time_ns"].std()
        df_new = grubbs_test(df_filtered)

        if df_new.shape[0] == df_filtered.shape[0]:  
            break

        df_filtered = df_new
        sd_trend.append(prev_std)  # store SD before removal

    return df_filtered, sd_trend

# plot standard deviation trend
def plot_sd_trend(sd_trend):
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(sd_trend)), sd_trend, marker="o", linestyle="-")
    plt.xlabel("Iteration")
    plt.ylabel("Standard Deviation")
    plt.title("Standard Deviation Trend (After Outlier Removal)")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    print("Fetching data from MySQL...")
    df_raw = fetch_data()

    print(f"Initial dataset size: {df_raw.shape[0]}")

    df_filtered_list = []
    sd_trend_list = []

    for operation in df_raw["crypto_operation"].unique():
        print(f"\nProcessing: {operation}")

        df_op = df_raw[df_raw["crypto_operation"] == operation].copy()
        df_filtered, sd_trend = remove_outliers(df_op)

        df_filtered_list.append(df_filtered)
        sd_trend_list.append(sd_trend)

        print(f"Final dataset size after outlier removal: {df_filtered.shape[0]}")

        plot_sd_trend(sd_trend)

    df_filtered_final = pd.concat(df_filtered_list, ignore_index=True)

    print("\nOutlier removal complete.")
    print(f"Final dataset size after removing all outliers: {df_filtered_final.shape[0]}")

    # generate dynamic file name with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"filtered_{TABLE_NAME}_{timestamp}.csv"

    # filepath path (
    save_dir = r"C:\Users\Karan\repos\CryptoGrubbsSD\.venv"
    save_path = os.path.join(save_dir, file_name)

    #  filtered data stored
    df_filtered_final.to_csv(save_path, index=False)
    print(f"Filtered data saved as: {save_path}")
