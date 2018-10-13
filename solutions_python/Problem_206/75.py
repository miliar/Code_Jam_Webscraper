# Solution to "Steed 2: Cruise Control" for Google Code Jam 2017
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys

def cases(inputFile):
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for _ in range(numCases):
            d, n = [int(x) for x in f.readline().split()]
            horses = [[int(x) for x in f.readline().split()]
                      for _ in range(n)]
            yield d, n, horses

def solve(d, n, horses):
    t = max(float((d - k))/s for k, s in horses)
    return d/t

with open(sys.argv[2], 'w') as f:
    for num, args in enumerate(cases(sys.argv[1])):
        f.write("Case #%d: %f\n"%(num+1, solve(*args)))
