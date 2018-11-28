#!/usr/bin/python3

n_cases = int(input())
for ctr in range(n_cases):
    n, arr = input().split()
    arr = [int(x) for x in arr]
    n_standing = 0
    n_added = 0
    for i, x in enumerate(arr):
        if n_standing < i:
            n_added += i - n_standing
            n_standing = i
        n_standing += x
    print('Case #%d: %d' % (ctr+1, n_added))
