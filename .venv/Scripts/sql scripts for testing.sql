
# ECDH_BENCHMARK 1000 Filtered/Unfiltered
SELECT
    crypto_operation,
    AVG(time_ns) AS mean_time_ns,
    STDDEV_POP(time_ns) AS stdev_sample,
    (STDDEV_POP(time_ns) / AVG(time_ns)) * 100 AS stdev_percentage
FROM filtered_ecdh_benchmark_1000_2025_02_12_12_21_09 -- Switch for unfiltered/filtered ( filtered_ecdh_benchmark_1000_2025_02_12_12_21_09 )
GROUP BY crypto_operation;

SELECT
    crypto_operation,
    AVG(time_ns) AS mean_time_ns,
    STDDEV_POP(time_ns) AS stdev_sample,
    (STDDEV_POP(time_ns) / AVG(time_ns)) * 100 AS stdev_percentage
FROM ecdh_benchmark_1000 -- Switch for unfiltered/filtered ( filtered_ecdh_benchmark_1000_2025_02_12_12_21_09 )
GROUP BY crypto_operation;




# kyber 1000 Filtered/Unfiltered
SELECT
    crypto_operation,
    AVG(time_ns) AS mean_time_ns,
    STDDEV_POP(time_ns) AS stdev_sample,
    (STDDEV_POP(time_ns) / AVG(time_ns)) * 100 AS stdev_percentage
FROM kyber_benchmark_1000 -- Switch for unfiltered/filtered ( filtered_ecdh_benchmark_1000_2025_02_12_12_21_09 )
GROUP BY crypto_operation;



SELECT
    crypto_operation,
    AVG(time_ns) AS mean_time_ns,
    STDDEV_POP(time_ns) AS stdev_sample,
    (STDDEV_POP(time_ns) / AVG(time_ns)) * 100 AS stdev_percentage
FROM filtered_kyber_benchmark_1000_2025_02_12_14_23_47 -- Switch for unfiltered/filtered ( filtered_ecdh_benchmark_1000_2025_02_12_12_21_09 )
GROUP BY crypto_operation;
