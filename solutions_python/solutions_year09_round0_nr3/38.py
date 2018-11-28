import string
import sys

N = int(sys.stdin.readline())
S = 'welcome to code jam'

def solve(s):
    ways = [1] + [0 for i in xrange(len(S))]
    for c in s:
        for (i,cS) in enumerate(S):
            if cS == c:
                ways[i+1] = (ways[i] + ways[i+1]) % 10000
    return ways[len(S)]

for n in xrange(N):
    print "Case #%d: %04d" % (n+1, solve(sys.stdin.readline()))
