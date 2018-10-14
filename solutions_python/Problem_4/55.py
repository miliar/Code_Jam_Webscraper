import sys

t = input()
for i in range(t):
    n = input()
    x = map(int, sys.stdin.readline().split())
    y = map(int, sys.stdin.readline().split())
    x.sort()
    y.sort()
    y.reverse()
    print 'Case #%d: %d' % (i+1, sum(xi * yi for (xi, yi) in zip(x,y)))
