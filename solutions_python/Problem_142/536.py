#!/usr/bin/env python3

################################################################################

def read_int():
    return int(input())

def read_words():
    return input().split()

def read_ints():
    return list(map(int,read_words()))

def read_floats():
    return list(map(float,read_words()))

################################################################################

import itertools as it

def groupify(s):
    result = []
    x = s[0]
    count = 0
    for c in s:
        if c==x:
            count+=1
        else:
            result.append((x,count))
            count = 1
            x = c
    result.append((x,count))
    return result

def all_same(xs):
    y = xs[0]
    for x in xs:
        if x != y:
            return False
    return True

def compute_group(g):
    n = len(g)
    s = sum(g)    
    v = round(s / n)
    
    return  sum( (abs(x - v) for x in g))

def compute(xs):
    n = len(xs)
    m = len(xs[0])
    result = 0
    for i in range(m):
        g = [ xs[j][i] for j in range(n) ]
        result += compute_group(g)
    return result

def solve(strings):
    n = len(strings)
    groups = [ groupify(s) for s in strings ]
    z = [ list(zip(*g)) for g in groups ]
    
    chars = [ zel[0] for zel in z ]
    nums  = [ zel[1] for zel in z ]

    if not all_same(chars):
        return "Fegla Won"

    return compute(nums)


if __name__ == "__main__":
    T = read_int()
    for c in range(T):
        N = read_int()
        strings = list(it.chain.from_iterable([ read_words() for _ in range(N)]))
        R = solve(strings)
        print("Case #{}: {}".format(c+1,R))
