# Wilcoxon Signed Rank Test and Standard Deviation Calculator

This script performs a One-Sample Wilcoxon Signed Rank Test and calculates the standard deviation for the data from six questions (Q1 to Q6) across eight participants (P1 to P8). The script compares each question's data to a specified hypothesised median (in this case, 3) and outputs the test statistic, p-value, and standard deviation for each question.

This script was used for my Usability Testing Module coursework.

## Prerequisites

Before running the script, make sure you have the necessary Python packages installed:

- `numpy`
- `scipy`

You can install these packages using pip:

```bash
pip install numpy scipy
```

## Usage

To use the script:

1. Clone this repository or download the script file.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:

```bash
python main.py
```

## Script Overview

- Data: The script uses predefined data from six questions (Q1 to Q6) across eight participants (P1 to P8).
- Hypothesised Median: The script uses a specified hypothesised median (3) for the Wilcoxon Signed Rank Test.
- Wilcoxon Signed Rank Test: The script performs a One-Sample Wilcoxon Signed Rank Test on each question's data against the hypothesised median. It calculates the differences between the data points and the hypothesised median and uses them to perform the test.
- Standard Deviation: The script calculates the standard deviation of each question's data using NumPy's np.std() function.
- Output: The script prints the test statistic, p-value, and standard deviation for each question's data.

## Output

After running the script, you will see the test statistic, p-value, and standard deviation for each question's data in the terminal output.

This should be the output given the current dataset:

```bash
Wilcoxon Signed Rank Test for Q1:
  Statistic: 0.0
  P-value: 0.014305878435429648
  Standard Deviation: 0.4330127018922193

Wilcoxon Signed Rank Test for Q2:
  Statistic: 0.0
  P-value: 0.0078125
  Standard Deviation: 0.4330127018922193

Wilcoxon Signed Rank Test for Q3:
  Statistic: 0.0
  P-value: 0.015186198557064549
  Standard Deviation: 0.6614378277661477

Wilcoxon Signed Rank Test for Q4:
  Statistic: 0.0
  P-value: 0.0078125
  Standard Deviation: 0.4330127018922193

Wilcoxon Signed Rank Test for Q5:
  Statistic: 0.0
  P-value: 0.0832645166635504
  Standard Deviation: 0.4841229182759271

Wilcoxon Signed Rank Test for Q6:
  Statistic: 0.0
  P-value: 0.0081509715935027
  Standard Deviation: 0.33071891388307384
```