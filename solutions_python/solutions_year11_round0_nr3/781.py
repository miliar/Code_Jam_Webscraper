#!/usr/bin/python
import sys

def read_ints():
    return [int(x) for x in raw_input().strip().split()]

def main():
    [T]=read_ints()
    for t in xrange(1,T+1):
        [N]=read_ints()
        C=read_ints()
        xor=0
        for ci in C:
            xor=xor^ci
        if xor != 0:
            print 'Case #%d: NO' % t
            continue
        print 'Case #%d: %d' % (t,sum(C)-min(C))

if __name__=='__main__':
    main()

