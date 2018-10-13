#!/usr/bin/env python
import pprint as pp

def read():
    line = raw_input() 
    line = raw_input() 
    s = line.split()
    data = [int(el)-1 for el in s]
    return data


def run_test():
    data = read()
    N = len(data)
    mapped = [0]*N

    res = 0
    cur = 0
    c = 0
    mi = -1
    while c<N:
        cur+=1
        c0 = 0
        mi+=1
        while mapped[mi]>0: mi+=1
        i = mi
        while mapped[i]==0:
            mapped[i] = cur
            i = data[i]
            c0 += 1
        if c0>1: res+=c0
        c+=c0
    return "%.6f"%res

def main():
    tests = int(raw_input())
    for test in xrange(tests):
        print "Case #%i: %s"%(test+1, str(run_test()))

main();
