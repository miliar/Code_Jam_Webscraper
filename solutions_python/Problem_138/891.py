
from copy import copy
import sys


if __name__ == '__main__':
    input = sys.stdin
    T = int(input.readline())
    for t in xrange(T):
        n = int(input.readline())
        a = sorted(map(float, input.readline().split()))
        b = sorted(map(float, input.readline().split()))
        a1, b1 = copy(a), copy(b)
        war = 0
        for i in a:
            gt = [x for x in b if x > i]
            if not len(gt):
                gt = b
                war += 1
            m = min(gt)
            b.remove(m)
        a, b = a1, b1
        dwar = 0
 #       print a
 #       print b
        while len(a):
            while len(a) and a[0] < b[0]:
                a.remove(a[0])
                b.remove(b[-1])
            while len(a) and a[0] > b[0]:
                dwar += 1
                a.remove(a[0])
                b.remove(b[0])
        print 'Case #%s: %s %s' % (t + 1, dwar, war)
