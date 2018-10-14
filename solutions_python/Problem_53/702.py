from __future__ import with_statement
import sys

class Snapper(object):
    def __init__(self, power, state=False):
        self.state = state
        self.power = power

    def __repr__(self):
        return "(s: %s, p: %s)" % ("ON" if self.state else "OFF",
                                         "ON" if self.power else "OFF")


with open(sys.argv[1]) as f:
    T = int(f.readline())
    for c in xrange(1, T+1):
        N, K = map(int, f.readline().split())
        snappers = [Snapper(i==0) for i in xrange(N)]
        for i in xrange(K):
            #print snappers
            power = True
            for s in snappers:
                if s.power:
                    s.state = not s.state
                s.power, power = power, power and s.state

        #print snappers
        s = snappers[-1]
        print "Case #%d: %s" % (c, "ON" if (s.power and s.state) else "OFF")
