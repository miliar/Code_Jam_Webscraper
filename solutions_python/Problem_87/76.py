#!/usr/bin/env python

import sys

def debug(*args, **kwargs):
    ags = map(str, args)
    kags = map(lambda xs: "%s: %s" % xs, kwargs.iteritems())
    print >>sys.stderr, ", ".join(ags) + ", ".join(kags)

def line():
    return sys.stdin.readline().strip()

def intline():
    return map(int, line().split())

def main(argv):
    T = int(line())
    for caseno in xrange(T):
        x,w,r,t,n = intline()
        paths = []
        for _ in xrange(n):
            paths.append(intline())
        paths.sort()
        dists = []
        for start,end,speed in paths:
            dists.append((speed, end - start))
        dists.append((0, x - sum([b for a,b in dists])))
        dists.sort()

        t = float(t)
        adjusted = []
        for speed,d in dists:
            if t <= 0:
                adjusted.append(float(d)/float(speed + w))
                continue
            subt = float(d)/float(speed + r)
            if subt > t:
                adjusted.append(t)
                adjusted.append((d - float(speed + r)*t)/float(speed + w))
            else:
                adjusted.append(subt)
            t -= subt
        print "Case #%d: %f" % (caseno + 1, sum(adjusted, 0.0))

if __name__ == "__main__":
    sys.exit(main(sys.argv))
