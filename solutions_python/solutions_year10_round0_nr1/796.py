#!/usr/bin/env python

def check_n_k(n,k):
    if k == 0:
        return False
    else:
        for i in xrange(n):
            if not k & (1 << i):
                return False
        return True

def parse(s):
    lines = s.split('\n')
    n_cases = int(lines[0])
    cases_seen = 0
    for ndx,l in enumerate(lines[1:]):
        pair = l.split()
        if len(pair) == 2:
            n,k = map(int,l.split())
            print "Case #%d:" % (ndx+1), ("OFF","ON")[check_n_k(n,k)]
            cases_seen += 1
    assert n_cases == cases_seen

if __name__ == '__main__':
    teststr = """4
1 0
1 1
4 0
4 47"""
    #s = teststr
    import sys
    infile = open(sys.argv[1])
    s = infile.read()
    infile.close()
    parse(s)
