from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random, string

def flip(x):
    if x == '-':
        return '+'
    return '-'

def sol(arr, k):

    l = len(arr)
    ans = 0

    i = 0
    while (i+k-1 <= l - 1):
        # print "UUU", i, ans, string.join(arr)
        if arr[i] == '-':
            ans += 1
            j = 0
            while j < k:
                arr[i+j] = flip(arr[i+j])
                j += 1
            # print "VVV", i, ans, string.join(arr)
        i += 1

    if '-' in arr:
        return "IMPOSSIBLE"

    return ans

T = int(stdin.readline())

for i in range(1,T+1):

    arr, k = stdin.readline().split()
    
    print "Case #" + str(i) + ":", 
    print sol(list(arr), int(k))
    
