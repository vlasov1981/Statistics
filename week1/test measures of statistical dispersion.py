import statistics


# q1
def q1():
    k = [67, 1, 50, 15, 34, 100, 23]

    for i in k:
        arr = [i + 1, 2 * i, 101]
        if statistics.median(arr) == statistics.mean(arr):
            print(f'k = {i}')


# q2
def q2():
    k = [3, 100, 1, 2]
    for i in k:
        arr = [i + 1, 2 * i, 101]
        print(arr)
        print(f"k = {i}, mode = {statistics.mode(arr)}")


# q3
# For 𝑘 = 50 and the sample (𝑘 + 1, 2𝑘, 101) the following is true:
def q3():
    k = 50
    arr = [k + 1, 2 * k, 101]
    print(statistics.mean(arr) < statistics.median(arr))
    print(statistics.mean(arr) > statistics.median(arr))


# q4 The probabilities of meeting with students from different faculties on campus are as follows.
import random
def q4():
    students = ['physical', 'economical', 'mathemat', 'psych']
    prob = [1 / 6, 1 / 4, 1 / 3, 1 / 4]
    counter = 0
    for k in range(10000):
        output = []
        for i in range(4):
            output.append(*random.choices(students, prob))
        if output.count('mathemat') >= 2:
            counter +=1
    print(counter/10000)
