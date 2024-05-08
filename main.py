from scipy.stats import wilcoxon
import numpy as np

# Data: each element in the list is the data for one question (Q1, Q2, Q3, Q4, Q5, Q6)
data = [
    [4, 4, 3, 4, 4, 3, 4, 4], # Q1 data
    [4, 4, 4, 4, 5, 4, 5, 4], # Q2 data
    [5, 5, 4, 5, 4, 3, 4, 4], # Q3 data
    [4, 4, 4, 4, 5, 4, 5, 4], # Q4 data
    [4, 3, 3, 4, 4, 3, 3, 3], # Q5 data
    [4, 4, 4, 4, 4, 3, 4, 4]  # Q6 data
]

# Hypothesised median
hypothesised_median = 3

# Loop through each question's data and perform the Wilcoxon Signed Rank Test
for i, question_data in enumerate(data):
    # Calculate the standard deviation of the data
    std_dev = np.std(question_data)

    # Subtract hypothesised median from each data point to create a list of differences
    differences = [x - hypothesised_median for x in question_data]

    # Perform the Wilcoxon Signed Rank Test on the differences
    stat, p_value = wilcoxon(differences)

    # Print the result
    print(f"Wilcoxon Signed Rank Test for Q{i + 1}:")
    print(f"  Statistic: {stat}")
    print(f"  P-value: {p_value}")
    print(f"  Standard Deviation: {std_dev}")
    print()
