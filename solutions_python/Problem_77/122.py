#!/usr/bin/python
# coding: utf-8

def main() :
    T = int(raw_input())
    for t in xrange(T) :
        N = int(raw_input())
        num = [ int(i) for i in raw_input().split() ]
        correct = num[:]
        correct.sort()
        m = len(filter(lambda x: num[x] != correct[x], xrange(N)))
        print 'Case #%d: %.20f' % (t + 1, m)

if __name__ == '__main__' :
    main()
