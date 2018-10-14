# Solution to "Oversized Pancake Flipper" for Google Code Jam 2017
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys

def cases(inputFile):
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for _ in range(numCases):
            yield f.readline().split()

def flip(pancakes, p, k):
    for x in range(p, p+k):
        if pancakes[x] == '+':
            pancakes[x] = '-'
        else:
            pancakes[x] = '+'

def solve(pancakes, k):
    k = int(k)
    pancakes = list(pancakes)
    l = len(pancakes)
    flips = 0
    for p in range(l-k + 1):
        if pancakes[p] == '-':
            flip(pancakes, p, k)
            flips += 1
    for p in range(l-k + 1, l):
        if pancakes[p] == '-':
            return 'IMPOSSIBLE'
    return str(flips)

with open(sys.argv[2], 'w') as f:
    for num, args in enumerate(cases(sys.argv[1])):
        f.write("Case #%d: %s\n"%(num+1, solve(*args)))
