import math
import queue

import collections

def divides_to(num):
    return math.ceil((num - 1) / 2), math.floor((num - 1) / 2)


def sequences_dict(num):
    sequences_dict = collections.OrderedDict()
    sequences_dict[num] = 1
    q = []
    q.insert(0, num)
    while len(q) > 0:
        sequence = q.pop()
        occurrences = sequences_dict[sequence]
        high, low = divides_to(sequence)
        if high > 0:
            if high not in sequences_dict:
                sequences_dict[high] = occurrences
            else:
                sequences_dict[high] += occurrences
            if high > 1 and high not in q:
                q.insert(0, high)
        if low > 0:
            if low not in sequences_dict:
                sequences_dict[low] = occurrences
            else:
                sequences_dict[low] += occurrences
            if low > 1 and low not in q:
                q.insert(0, low)
    return sequences_dict

def max_min_lr(n, k):
    sequences = sequences_dict(n)
    sequences_list = list(sequences.items())
    idx = 0
    while k > 0:
        k -= sequences_list[idx][1]
        idx += 1
    return divides_to(sequences_list[idx - 1][0])

t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    mini, maxi = max_min_lr(n, k)
    print("Case #{}: {} {}".format(i, mini, maxi))
