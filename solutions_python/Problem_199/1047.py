import numpy as np

def find_fewest_flips(bits, n, k):
#     bits is numpy array
    arrays = [np.array([0]*i + [1]*k + [0]*(n - k - i)) for i in range(n - k + 1)]
    counter = 0
    for i in xrange(n - k + 1):
        if (bits[i] % 2) == 0:
            bits += arrays[i]
            counter += 1
    for j in range(n - k + 1, n):
        if (bits[j] % 2) == 0: return "IMPOSSIBLE"
    return counter

def get_bits(string):
    return np.array([0 if string[i] == "-" else 1 for i in xrange(len(string))])


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    inp = raw_input().split(" ")
    bits = get_bits(inp[0])
    n = len(inp[0])
    k = int(inp[1])
    print "Case #{}: {}".format(i, find_fewest_flips(bits, n, k))
