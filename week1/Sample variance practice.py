import statistics

# q1 Find unbiased sample variance
"""x = [9, 3, 8, 5, 9]
x_mean = statistics.mean(x)
var_unbiased = 0
for i in x:
    var_unbiased += (i - x_mean)**2
var_unbiased /= (len(x)-1)
print(var_unbiased)

print(statistics.variance(x))
"""
# q2 What’s the right conclusion about variances v1 and v2 of these samples:
"""x1 = [2, 8, 3, 5, 2, 5, 2, 6, 3, 5, 2, 1]
x2 = [7, 13, 8, 10, 7, 10, 7, 11, 8, 10, 7, 6]
print(statistics.variance(x1))
print(statistics.variance(x2))"""


