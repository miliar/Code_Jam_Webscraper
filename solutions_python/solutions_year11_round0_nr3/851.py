from sys import *
import itertools

def findsubsets(S,m):
    return set(itertools.combinations(S, m))            

def SumXor(items):
    num = 0
    for i in items:
        num ^= i
    return num

def solve(_, items, c):
    items.sort()
    items.reverse()
    sumXor = SumXor(items)
    if sumXor % 2 != 0:
        print "Case #%d: NO" %(_+1)
        return
    values = []
    for length in range(c - 1, 0, -1):
        for subset in itertools.combinations(items, length):
            num = SumXor(subset)
            if num ^ sumXor == num:
                values.append(sum(subset))
    if len(values) != 0:
        MaxValue = max(values)
        print "Case #%d: %d" %(_+1, MaxValue)
        return
    else:
        print "Case #%d: NO" %(_+1)
        return
    
    
    
##    for i in xrange(len(items)):
##        for j in xrange(i+1,len(items)):
##            if items[i] + items[j] == c:
##                print "Case #%d: %d %d" %(_+1,i+1,j+1)%0.2f 

cases = int(raw_input())
for _ in xrange(cases):
    c = int(raw_input())
    items = map(int,stdin.readline().split())
    solve(_, items, c)
