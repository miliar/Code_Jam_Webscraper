import sys


def solve(xs):
    t = 0
    for i in xrange(len(xs)):
        if i + 1 != xs[i]:
            t += 1
    return t


T = int(raw_input())
for t in xrange(T):
    sys.stdin.readline()

    line  = sys.stdin.readline().strip()
    xs = map(int, line.split(' '))

    print 'Case #%d: %.6f' % (t+1, solve(xs))
