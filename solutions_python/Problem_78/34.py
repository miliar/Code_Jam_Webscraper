#!/usr/bin/env python
# encoding: utf-8
"""
Free Cell - smells like gcd

"""

import sys, time

# debug helper function
DEBUG = True
_debugf = open('/tmp/debug.log', 'w', 0)

def _debug(s):
    if not DEBUG: return
    if type(s) != str: s = repr(s)  
    _debugf.write("%9.3f - %s\n" % (time.clock(), s))



#problem specific functions

def parseInput(f):
     return map(int, f.readline().split())

def getStep(P):
    for i in range(100):
        t = P * (i+1) / 100.0
        if not (t % 1):
            return (i+1)
    
def main(args):
    # _debug(args)
    N, Pd, Pg = args
    ret = "Broken"
    if (Pg == 100 and Pd != 100) or (Pd>0 and Pg==0): return ret
    ret = getStep(Pd) <= N and "Possible" or ret
    return ret

if __name__ == "__main__":
    if len(sys.argv)==1:
        filename = 'test.in'
    else:
        filename = sys.argv[1]
    
    _debug("Starting %s" % filename)
    f = open(filename)
    cases = int(f.readline())
    for case in range(cases):
        args = parseInput(f)
        print "Case #%i: %s" % (case+1, main(args))
    _debug("Done")