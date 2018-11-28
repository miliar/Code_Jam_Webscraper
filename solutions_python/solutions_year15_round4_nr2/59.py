import sys
import random



def foo(ifile):
    n, v, t = [float(x) for x in ifile.readline().split()]
    n = int(n)
    vs = [0.0] * n
    ts = [0.0] * n
    for i in range(n):
        words = ifile.readline().split()
        vs[i] = float(words[0])
        ts[i] = float(words[1])
    if n == 1:
        if t != ts[0]:
            return 'IMPOSSIBLE'
        return '%.10f' % (v/vs[0])
    if n == 2:
        tmin = min(ts[0], ts[1])
        tmax = max(ts[0], ts[1])
        if t < tmin or t > tmax:
            return 'IMPOSSIBLE'
        if tmin == tmax:
            return '%.10f' % (v/(vs[0]+vs[1]))

        v0 = v * (ts[1]-t)/(ts[1]-ts[0])
        v1 = v - v0
        return '%.10f' % (max(v0/vs[0], v1/vs[1]))

    return 18.975332068


def main():
    ifile = sys.stdin
    n = int(ifile.readline())
    for i in range(n):
        print 'Case #%d: %s' % (i+1, foo(ifile))
        sys.stdout.flush()

main()

