#!/usr/bin/env python
import pprint as pp

def read():
    line = raw_input() 
    s = line.split()
    # data = [int(el) for el in s]
    return s

def next(t0,p0,p,to):
    t = max(t0 + abs(p-p0)+1, to+1)
    return t, p

def run_test():
    data = read()
    N = int(data[0])
    to, tb = 0, 0 # time
    po, pb = 1, 1 # pos
    for i in xrange(N):
        p = int(data[2*i+2])
        if data[2*i+1]=='O':
            to, po = next(to,po,p,tb)
        else:
            tb, pb = next(tb,pb,p,to)
        # print "B: pos=%d time=%d \tO: pos=%d time=%d"%(pb,tb,po,to)
    return max(tb,to)

def main():
    tests = int(raw_input())
    for test in xrange(tests):
        print "Case #%i: %s"%(test+1, str(run_test()))

main();
