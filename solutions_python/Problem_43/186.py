#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys, psyco
psyco.full()
rdl = sys.stdin.readline


class aliensys(object):
    def __init__(self, stringa):
        self.symbols = list(stringa)
        self.N = len(self.symbols)
    def a2d(self, n):
        s = 0
        n = list(n)
        n.reverse()
        for i in xrange(0, len(n)):
            s += self.symbols.index(n[i])*(self.N**i)
        return s
    def d2a(self, n):
        s = ''
        while n>=1:
            r = n%self.N
            n/=self.N
            s = self.symbols[r]+s
        return s
    def convert(self, n, target): # target must be an aliensys
        to = self.a2d(n)
        return target.d2a(to)

def process(case):
    """precessing case #"""
    #[int(x) for x in rdl.split()]
    code = rdl().replace('\n','')
    d = {}
    symbols = '1023456789abcdefghijklmnopqrstuvwxyz'
    symbol = 0
    trans = ''
    for s in code:
        if not s in d: 
            d[s] = symbols[symbol]
            symbol += 1
        trans += d[s]
    base = len(d)
    if base == 1: base = 2
    #print trans, base
    return int(trans, base)
        


cases = int(rdl())
for case in xrange(1, cases+1):
    print "Case #%d:"%case, process(case)
