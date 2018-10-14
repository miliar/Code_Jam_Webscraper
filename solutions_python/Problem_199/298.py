from sys import stdin
from bisect import bisect
import sys
if len(sys.argv) > 1:
    sys.stdout = open(sys.argv[1], 'w')

def each_case(S, K):
    flipper_ends = []
    position = 0
    for i, pancake in enumerate(S[:-K+1]):
        position = bisect(flipper_ends, i, position)
        if (position & 1) ^ (len(flipper_ends) & 1) ^ (pancake == '-'):
            flipper_ends.append(i+K)

    for j, pancake in enumerate(S[-K+1:]):
        position = bisect(flipper_ends, len(S)-K+1+j, position)
        if (position & 1) ^ (len(flipper_ends) & 1) ^ (pancake == '-'):
            return 'IMPOSSIBLE'

    return len(flipper_ends)

T = int(stdin.readline())
for t in xrange(1,T+1):
    S, K = stdin.readline().split()
    print 'Case #{}: {}'.format(t, each_case(S, int(K)))
