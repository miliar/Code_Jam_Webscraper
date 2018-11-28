import sys
import collections
import math

def rl():
    return tuple(map(int, raw_input().strip().split()))

def solve(n, p):
    #print '====== ' + str(locals())
    m1 = sum(p[i]-p[i+1] for i in xrange(len(p)-1) if p[i+1]<p[i])
    mm = max([p[i]-p[i+1] for i in xrange(len(p)-1) if p[i]>p[i+1]] + [0])
    m2 = sum(p[i] if p[i]<mm else mm for i in xrange(len(p)-1))
    return '{0} {1}'.format(m1, m2)

if __name__ == '__main__':
    for case in range(int(raw_input())):
        print 'Case #%d: %s' % (case+1, solve(int(raw_input().strip()), rl()))