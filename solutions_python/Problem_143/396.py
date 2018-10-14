from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random

T = int(stdin.readline())

for i in range(1,T+1):
    
    A, B, K = map(int, stdin.readline().split(' '))

    print "Case #" + str(i) + ":", 
    # print A, B, K

    ans = 0

    for a in range(0, A):
        for b in range(0, B):

            res = a & b

            if res < K:
                ans += 1

    print ans