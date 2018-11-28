import time
from queue import PriorityQueue
from collections import Counter


def last_spacing_slow(n, k):
    stalls = [0] * (n + 2)
    stalls[0] = stalls[-1] = 1
    for i in range(k):

        l_best = -1
        r_best = -1
        best = -1
        for j, stall in enumerate(stalls):
            if stall != 0:
                continue

            left = 0
            while stalls[j - (left + 1)] == 0:
                left += 1
            right = 0
            while stalls[j + right + 1] == 0:
                right += 1
            if min(l_best, r_best) < min(left, right) or (
                            min(l_best, r_best) == min(left, right) and max(l_best, r_best) < max(left, right)):
                best = j
                l_best, r_best = left, right
        # print(best, l_best, r_best, best < 50)
        # print(i, best < 50)
        stalls[best] = 1
        # print(best, best < n // 2, "".join(map(str, stalls)), i, (min(l_best, r_best), max(l_best, r_best)), )
    return max(l_best, r_best), min(l_best, r_best)


def last_spacing_medium(n, k):
    intervals = PriorityQueue()
    intervals.put(-n)
    for _ in range(k):
        largest = -intervals.get()
        left = (largest - 1) // 2
        right = largest - 1 - left
        intervals.put(-left)
        intervals.put(-right)
    return max(left, right), min(left, right)


def last_spacing_fast(n, k):
    intervals = Counter([n])
    while k > 0:


        largest = max((+intervals).keys())
        count = intervals[largest]



        left = (largest - 1) // 2
        right = largest - 1 - left

        if k - count <= 0:
            return max(left, right), min(left, right)
        k -= count
        intervals[largest] = 0
        intervals[left] += count
        intervals[right] += count

        # return max(left, right), min(left, right)


# def which_way(k):
#     my_k == k - 1
#     exponent = 1
#
#     while True:
#         if k < 2 ** (exponent - 1):
#             return
#
#
# def last_spacing(n, k):
#
#     if n < 1000 or k == 1:
#         return last_spacing_medium(n, k)
#
#
#
#
#
#
#
#     left = (n - 1) // 2
#     right = n - 1 - left





# n = 1000000000000000000
# k = n//4
# # print(last_spacing_slow(n, k))
# # start = time.time()
# # print(last_spacing_medium(n, k))
# # print(time.time() - start)
# start = time.time()
# print(last_spacing_fast(n, k))
# print(time.time() - start)


# INPUT = "TestInput"
# OUTPUT = "TestOutput"

# INPUT = "SmallInput1"
# OUTPUT = "SmallOutput1"

# INPUT = "SmallInput2"
# OUTPUT = "SmallOutput2"


INPUT = "LargeInput"
OUTPUT = "LargeOutput"

start = time.time()
with open(INPUT, "r") as input_file:
    with open(OUTPUT, "w") as output_file:
        output_file.truncate()

        t = int(input_file.readline())
        for i in range(t):
            print(i, t, time.time() - start)
            stalls, people = input_file.readline().split()
            stalls, people = int(stalls), int(people)
            min_space, max_space = last_spacing_fast(stalls, people)
            output_file.write(f"Case #{i+1}: {min_space} {max_space}\n")
end = time.time()

print(start, end, end - start)
