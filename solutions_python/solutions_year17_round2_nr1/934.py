from sys import stdin
import sys
if len(sys.argv) > 1:
    sys.stdout = open(sys.argv[1], 'w')

def each_case():
    D, N = map(int, stdin.readline().split())
    max_time = 0.
    for i in xrange(N):
        K, S = map(int, stdin.readline().split())
        time = (D-K)/float(S)
        if max_time < time:
            max_time = time
    return D / max_time

T = int(stdin.readline())
for t in xrange(1,T+1):
    print 'Case #{}: {}'.format(t, each_case())
