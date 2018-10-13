# Solution to "Bathroom Stalls" for Google Code Jam 2017
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys, heapq

def cases(inputFile):
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for _ in range(numCases):
            yield [int(x) for x in f.readline().split()]

def solve(n, k):
    people = 1
    while (2*people <= k):
        people *= 2
    people -= 1
    run = (n - people)/(people + 1)
    numBigger = n - people - run*(people+1)
    if numBigger >= k - people:
        run += 1
    if run%2 == 0:
        return run/2, run/2 - 1
    else:
        return run/2, run/2

with open(sys.argv[2], 'w') as f:
    for num, args in enumerate(cases(sys.argv[1])):
        result = ' '.join(str(x) for x in solve(*args))
        f.write("Case #%d: %s\n"%(num+1, result))
