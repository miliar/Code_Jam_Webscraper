#!/usr/bin/python2

from math import sqrt, ceil

def ispol(n):
    s = str(n)
    l = len(s)
    for i in range(l / 2):
        if s[i] != s[l - i - 1]:
            return False
    return True

def grange(a, b):
    lb = int(sqrt(b))
    la = int(ceil(sqrt(a)))
    n = 0
    for x in range(la, lb + 1):
        if ispol(x) and ispol(x * x):
            n += 1
    return n

def bsearch(data, l, u, val, islower):
    if u < l:
        return None
    if u - l < 2:
         if islower:
             return data[l] if data[u][0] > val else data[u]
         else:
             return data[u]
    p = int((u + l) / 2)
    if data[p][0] == val:
        return data[p]
    if data[p][0] > val:
        return bsearch(data, l, p, val, islower)
    if data[p][0] < val:
        return bsearch(data, p, u, val, islower)
            
    
def sorve(a, b, cache):
    lb = int(sqrt(b))
    la = int(ceil(sqrt(a)))
    na = bsearch(cache, 0, len(cache) - 1, la, True)
    nb = bsearch(cache, 0, len(cache) - 1, lb, True)
    return nb[1] - na[1] + ( 0 if na[0] < la else 1)
    
def precalc(m):
    lb = int(sqrt(m))
    cache = [(0,0)]
    n = 0
    for x in xrange(1, lb + 1):
        if ispol(x) and ispol(x * x):
            n += 1
            cache.append((x, n))
    return cache

if __name__=="__main__":
#    cache = [(0, 0), (1, 1), (2, 2), (3, 3), (11, 4), (22, 5), (101, 6), (111, 7), (121, 8), (202, 9), (212, 10), (1001, 11), (1111, 12), (2002, 13), (10001, 14), (10101, 15), (10201, 16), (11011, 17), (11111, 18), (11211, 19), (20002, 20), (20102, 21), (100001, 22), (101101, 23), (110011, 24), (111111, 25), (200002, 26), (1000001, 27), (1001001, 28), (1002001, 29), (1010101, 30), (1011101, 31), (1012101, 32), (1100011, 33), (1101011, 34), (1102011, 35), (1110111, 36), (1111111, 37), (2000002, 38), (2001002, 39)]

    f = file("fair.case");
    t = int(f.readline())
    pairs = []
    rline = lambda : [int(v) for v in f.readline().split(' ')]
    m = 0
    for i in range(t):
        a, b = rline()
        pairs.append((a,b))
        m = max(m, b)
    cache = precalc(m)
    for i in range(t):
        a, b = pairs[i]
        print "Case #%d:" % (i + 1), sorve(a, b, cache)
#        if sorve(a, b, cache) != grange(a, b):
#            raise "aeouo"
#        print "Case #%d:" % (i + 1), grange(a, b)
#    print cache
#    cache = [(1,2), (5,10), (9,0), (100,0), (140, 3), (400,0)]
#    print bsearch(cache, 0, len(cache) - 1, 141)

    
