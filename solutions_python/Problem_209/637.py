from itertools import combinations
from math import pi

def calculate(cakes):
    cakes.sort(key = lambda x:x[0])
    radius = cakes[-1][0]
    result = 0
    for i in cakes:
        result += 2*i[1]*i[0]
    result += radius*radius
    return result*pi

def solve():
    n,k = map(int, raw_input().strip().split())
    cakes = []
    for i in xrange(n):
        cakes += [map(int, raw_input().strip().split())]
    m = 0
    for i in combinations(cakes, k):
        m = max(m, calculate(list(i)))
    return "%.7f"%m

if __name__=="__main__":
    for i in xrange(input()):
        print "Case #"+str(i+1)+": "+str(solve())
