
import sys
import copy

def tryup(a):
    i = 0
    n = len(a)
    j = n - 1


def solve(case, f):
    n = int(f.readline())
    a = map(int, f.readline().split())
    rez = float('inf')
    b = copy.copy(a)
        #print b
    sol = 0
    for i in xrange(n):
        mpos = -1
        m = float('inf')
        for j in xrange(len(b)):
            if m > b[j]:
                m = b[j]
                mpos = j
        sol += min(len(b) - mpos - 1, mpos)
        b.remove(m)
    return sol


if __name__ == "__main__":
    f = sys.stdin

    t = int(f.readline())
    for _t in xrange(t):
        rez = solve(_t, f)
        print 'Case #%s: %s' % (_t + 1, rez)
