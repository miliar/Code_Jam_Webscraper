# -*- coding: utf-8 -*-
from __future__ import division, print_function
from math import sqrt, ceil, floor
from gmpy2 import is_square, isqrt
from itertools import product, combinations, chain


def parse(f):
    lst = []
    f.next()
    for l in f:
        N = int(l.split()[0])
        K = int(l.split()[1])
        lst.append((N, K))
    return lst

def brute(N, K):
    l = [1]+[0]*N+[1]
    for x in range(K):
        minLR = 0
        maxLR = 0
        best_k = 1
        for k in range(1, N+1):
            if(l[k] == 0):
                left1 = next((i for i in range(1,N+3) if l[k-i] == 1))
                right1 = next((i for i in range(1,N+3) if l[k+i] == 1))
                Lk = left1-1
                Rk = right1 - 1
                if(min(Lk, Rk) > minLR):
                    minLR = min(Lk, Rk)
                    maxLR = max(Lk, Rk)
                    best_k = k
                elif(min(Lk, Rk) == minLR and max(Lk, Rk) > maxLR):
                    maxLR = max(Lk, Rk)
                    best_k = k
        l[best_k] = 1

    return(maxLR, minLR)
            
    
def bathroom(N, K):
    # donne le niveau où K s'arrête
    p = K.bit_length() - 1  # 2^p <= K
    reste = K - 2**p

    # line p of the tree
    previous_line = {N: 1}
    line = previous_line
    for k in xrange(p):
        line = {}
        for a in previous_line:
            v = previous_line[a]
            if(a % 2 == 1):
                if (a>>1) in line:
                    line[a>>1] += 2*v
                else:
                    line[a>>1] = 2*v
            else:
                if (a>>1) in line:
                    line[a>>1] += v
                else:
                    line[a>>1] = v
                if ((a>>1) - 1) in line:
                    line[(a>>1)-1] += v
                else:
                    line[(a>>1)-1] = v
        previous_line = line
    key = line.keys()
    key.sort()
    key = key[::-1]
    print(line, reste)
    x = 0
    one_before = key[0]
    for a in key:
        x += line[a]
        if(x > reste):
            one_before = a
            break
    
    maxL = one_before >> 1
    minL = maxL - (1-(one_before%2))
    return (maxL, minL)


def output(fw, inlst):
    for i, a in enumerate(inlst):
        print(i, a)
        maxL, minL = bathroom(*a)
        # maxLt, minLt = brute(*a)
        # if(maxL != maxLt or minL != minLt):
        #     print("ERROR : ", a)
        #     print(maxL, minL)
        #     print(maxLt, minLt)
        print("Case #{}: {} {}\n".format(i+1, maxL, minL))
        fw.write("Case #{}: {} {}\n".format(i+1, maxL, minL))


f = open("C-large.in", 'r')
fw = open("C-large.out", 'w')
# f = open("C-test.in", 'r')
# fw = open("C-test.out", 'w')

output(fw, parse(f))
