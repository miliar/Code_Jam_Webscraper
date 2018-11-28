#!/usr/bin/env python

import sys

def line():
    return sys.stdin.readline().strip()

def intline():
    return map(int, line().split())

def main(argv):
    t = int(line())
    for caseno in xrange(t):
        n,l,h = intline()
        freqs = intline()
        lowest = l
        for guess in xrange(l,h+1):
            found = True
            for f in freqs:
                if guess % f != 0 and f % guess != 0:
                    found = False
                    break
            if found:
                print "Case #%d: %d" % (caseno + 1, guess)
                break
        if not found:
            print "Case #%d: NO" % (caseno + 1)
        
            

if __name__ == "__main__":
    sys.exit(main(sys.argv))
