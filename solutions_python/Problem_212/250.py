# Solution to "Fresh Chocolate" for Google Code Jam 2017
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys

def cases(inputFile):
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for _ in range(numCases):
            n, p = [int(x) for x in f.readline().split()]
            yield n, p, [int(x) for x in f.readline().split()]

def same(n, p):
    return n/p + (n%p != 0)

def solve(n, p, groups):
    remainders = [0]*p
    for x in groups:
        remainders[x%p] += 1
    fresh = remainders[0]
    if p == 2:
        fresh += same(remainders[1], p)
    elif p == 3:
        if remainders[1] <= remainders[2]:
            a, b = remainders[1], remainders[2]
        else:
            a, b = remainders[2], remainders[1]
        fresh += a
        b -= a
        fresh += same(b, p)
    elif p == 4:
        fresh + same(remainders[2], 2)
        if remainders[1] <= remainders[3]:
            a, b = remainders[1], remainders[3]
        else:
            a, b = remainders[3], remainders[1]
        fresh += a
        b -= a
        fresh += same(b, p)
        if (b%p != 0) and (remainders[2]%2 != 0):
            fresh -= 1 
    return fresh

with open(sys.argv[2], 'w') as f:
    for num, args in enumerate(cases(sys.argv[1])):
        f.write("Case #%d: %d\n"%(num+1, solve(*args)))
