#!/usr/bin/python3

from sys import argv
from itertools import permutations

from collections import defaultdict
def hash(): return defaultdict(hash)

def cycles(vals):
    r = []
    for i in range(0, len(vals)):
        n, l = i, 0
        while vals[n] != 0:
            newn = vals[n] - 1
            vals[n] = 0
            l += 1
            n = newn
        if l > 1:
            r.append(l)
    return r

def expected(length):
    if length <= 1:
        return 0.0
    elif length == 2:
        return 2.0

def exp(length):
    if length in exp.cache:
        return exp.cache[length]
    n, t, d, vals = 0, 0, 0, range(1, length+1)
    for p in permutations(vals):
        n += 1
        c = cycles(list(p))
        if len(c) == 1 and c[0] == length:
            d += 1   # this counts derangements
        else:
            for i in c:
                t += exp(i)
    # now we need to solve the equation:
    # exp(length) = t/n + exp(length)*(n-d)/n + 1
    # exp(length)(1-(n-d)/n) = t/n + 1
    # exp(length) = (t/n+1) / (1-(n-d)/n)
    print('n={}, t={}, d={}'.format(n,t,d))
    r = (t/n+1) / ((n-d)/n)
    exp.cache[length] = r
    return r

exp.cache = hash()
exp.cache[0] = 0
exp.cache[1] = 0
exp.cache[2] = 2
# exp.cache[3] = 6
# exp.cache[4] = 16
# exp.cache[5] = 40
# exp.cache[6] = 96
# exp.cache[7] = 224
# exp.cache[8] = 512
# exp.cache[9] = 1152
# exp.cache[10] = 2560

def goro(vals):
    r, c = 0, cycles(vals)
    for l in c:
        r += l
    return r

if __name__ == '__main__':
    infile = open(argv[1])
    cases = int(infile.readline())
    for i in range(0, cases):
        n = int(infile.readline())
        vals = list(map(int, infile.readline().split()))
        print('Case #{}: {:.6f}'.format(i+1, goro(vals)))
