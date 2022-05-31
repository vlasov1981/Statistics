import statistics
import math
import numpy as np

# q1 Find 0.1-quantile of random variable with probability density function given by formula:
"""print(1 - 3 / math.sqrt(10))

# q2 Consider sample (1,1,2,3,5,5,6). Use function numpy.quantile to find 0.2-quantile of this sample.

x = [1, 1, 2, 3, 5, 5, 6]
print(np.quantile(x, 0.2))"""


# Quartiles skill test
# q1 Consider sample (−x,−3,−1,0,1,3,x). How large can you make IQR (inter-quartile range) by choosing x?
# Use definition of quartiles from the videos
def q1():
    for i in range(0, 100, 10):
        y = [-i, -3, -1, 0, 1, 3, i]
        print(statistics.variance(y))


# q2 Assume you have 7-elements sample and you know that its IQR is 2. (Use definition of quartile from the videos.)
# What is the smallest possible value sample standard deviation (square root of unbiased sample variance) can take?
# Enter five digits after decimal point.
def q2():
    x = [3, 3, 4, 4, 4, 5, 5]
    print(statistics.stdev(x))
q2()  # 0.816496580927726
