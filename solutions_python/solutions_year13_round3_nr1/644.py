#!/usr/bin/env python
# coding=utf-8

import sys
import re

def affects(totallen, span, n):
    # How many substrings of length n contain the characters between start and end?
    start, end = span
    l = end-start
    if l > n:
        return 0
    else:
        ret = min(start+1, totallen-end+1, n-l+1)
        #print totallen, span, n, ret
        return ret


def solve(name, n):
    #print name, n
    matches = re.finditer('(?=([bcdfghjklmnpqrstvwxyz]{%d}))' % n, name)
    results = [(match.group(1), match.span(1)) for match in matches]
    #print results
    res = sum(min(sum(affects(len(name), res[1], i) for res in results), len(name)-i+1) for i in xrange(1,len(name)+1))
    return res

def solve_dumb(name, n):
    res = 0
    for start in xrange(len(name)):
        for end in xrange(start, len(name)):
            sub = name[start:end+1]
            if re.search('[bcdfghjklmnpqrstvwxyz]{%d}' % n, sub) is not None:
                res += 1
    return res


def main():
    with open(sys.argv[1]) as f:
        f.readline()
        for i, line in enumerate(f):
            name, n = line.strip().split()
            res = solve_dumb(name, int(n))
            print 'Case #%d: %d' % (i+1, res)

if __name__ == '__main__':
    main()
