import sys
#import math

with open(sys.argv[1]) as infile:
    input = infile.readlines()

T = int(input[0])

result = []


def flip(cakes, i, K):
    c = cakes[:i]
    for j in range(i, i + K):
        if cakes[j] == '-':
            c+= '+'
        else:
            c+= '-'
    c += cakes[(i + K):]
    return c


def solve_cakes(cakes, K):

    N = len(cakes)
    flips = 0
    for i in range(N - K + 1):
        if cakes[i] == '-':
            cakes = flip(cakes, i, K)
            flips += 1
    if cakes[-K:] != K * '+':
        return 'IMPOSSIBLE'

    return flips


for line in input[1:]:
    cakes, K = line.split()[:2]
    K = int(K)
    result.append(solve_cakes(cakes, K))

with open(sys.argv[1].split('.')[0] + '.out', 'w') as outfile:
    for i, r in enumerate(result):
        outfile.write("Case #%s: %s \n" % (i + 1, r))
