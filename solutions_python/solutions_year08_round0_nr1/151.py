import os
from sys import stdin
import sys

def readint():
    return int(sys.stdin.readline())

def save_the_universe():
    cases = readint()
    for i in xrange(cases):
        print "Case #%d: %d" % (i+1, do_one_case())
    pass

def do_one_case():
    engines = read_engines()
    queries = read_queries()
    mins = dict([(s,0) for s in engines])
    for q in queries:
        if mins.has_key(q):
            m = min([v for (k,v) in mins.items() if k != q])
            mins[q] = m + 1
    return min(mins.values())

def read_engines():
    return read_ct_and_lines()

def read_queries():
    return read_ct_and_lines()

def read_ct_and_lines():
    n = readint()
    return [stdin.readline().rstrip() for i in xrange(n)]

if __name__ == '__main__':
    save_the_universe()
