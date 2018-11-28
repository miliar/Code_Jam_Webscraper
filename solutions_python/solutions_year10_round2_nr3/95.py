
import itertools
from bisect import bisect_left

def isPure(list, n):
    currentNum = n
    index = -1
    while(index != 0):
        index = bisect_left(list, currentNum)
        if index>=len(list) or list[index] != currentNum:
            return False
        currentNum = index+1
    return True

def solve(f):
    n = int(f.readline())
    pure = 0
    for j in xrange(1, n):
        for i in itertools.combinations(xrange(2, n+1), j):
            if isPure(i, n):
                pure += 1
    
    return pure % 100003


with open('C-small.in', 'r') as f:
    T = int(f.readline())
    results = [solve(f) for i in xrange(T) ]
    for i in xrange(T):
        print "Case #%d: %s" % (i+1, results[i])