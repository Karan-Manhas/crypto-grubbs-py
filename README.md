# CryptoGrubbsSD
This Python script analyzes cryptographic benchmarking data (specifically from Kyber ) stored in a MySQL database, using Grubbs' test to iteratively detect and remove statistical outliers from timing measurements. 

This project takes the benchmarked cryptographic operations (like key generation, encryption, and decryption) data by fetching data from a MySQL database, and applying  **Grubbs' Test** to iteratively detect and remove outliers based on execution time.

The goal of this project is to clean and stabilize cryptographic benchmark results by applying statistical methods to identify noisy or extreme values that skew performance analysis. Additionally to 

---


## Why These Stats?

### Convergence Analysis / Stability Analysis

Used to evaluate the **reliability and precision** of cryptographic performance metrics. This script:

- Measures **mean execution time** and **standard deviation** over multiple iterations.
- Identifies when **additional iterations do not significantly reduce variance**.
- Ensures results are **statistically stable** (i.e., not fluctuating across runs).

### Key Statistical Methods Used

- **Mean**: Average execution time per iteration count.
- **Standard Deviation**: Measures spread/variability in execution time.
- **Coefficient of Variation**: Relative standard deviation to determine statistical stability.
- **Convergence Testing**: Verifies that increasing iterations reduces variability.

### Why Are These Important?

- **Statistical Stability**: Prevents misleading results due to random spikes.
- **Compute Resource Efficiency**: Avoids over-benchmarking, saving time and compute.
- **Optimal Iteration Count**:
  - Too few = unreliable.
  - Too many = wasted time.
  - Goal: Find the point where **standard deviation plateaus**.
- **Repeatable Evaluation**: Ensures reliable, consistent performance metrics for cryptographic algorithms like **Kyber** and **ECDH**.

##  Project Structure

- .venv/Scripts/activate is how to activate the virtual environment
- .venv/Scripts/script.py is to be execute din the environment via `python script.py` once virtual environment is running

## Prequisites

- MySQL DB Connection Details and SetUp
- Benchmark data (copy is already obtained in ".venv\kyber_benchmark_1000" )
- Python 3.8+
- MySQL Server (running locally or remotely)
- MySQL table structure should include:

###  Ensure to set configurations here
```bash
DB_USER = "your_user"
DB_PASSWORD = "your_password"
DB_NAME = "crypto"
TABLE_NAME = "kyber_benchmark_1000"
DB_URL = "localhost"
DB_PORT = 3306
```

## How to set up 

### 1. Clone the repository: 
```bash
git clone https://github.com/Karan-Manhas/crypto-grubbs-py.git
cd crypto-grubbs-py
```

### 2. create & activate the virtual environment

```bash
python -m venv .venv
# then activate it:
.venv\Scripts\activate    # Windows
# OR
source .venv/bin/activate     # macOS/Linux
```

### 2. create & activate the virtual environment

```bash
python .venv/Scripts/script.py
```

### 3. Check Output

- Plots showing standard deviation trend as outliers are removed (Example found here: `crypto-grubbs-py\example output.png`)
- Console logs showing intial and final dataset size
- Cleaned data saved to CSV file named like: `filtered_kyber_benchmark_1000_YYYY-MM-DD_HH-MM-SS.csv`


crypto-grubbs-py\example output.png