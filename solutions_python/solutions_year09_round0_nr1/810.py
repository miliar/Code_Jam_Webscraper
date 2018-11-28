#!/usr/bin/env python

import sys, re

def count_matches(pat, dict):
    _pattern = pat.replace('(', '[')
    _pattern = _pattern.replace(')', ']')
    pattern = re.compile(_pattern)
    count = 0
    res = pattern.finditer(dict)
    while True:
        try:
            res.next()
            count += 1
        except StopIteration:
            break
    return count
    

if __name__=='__main__':
    try:
        input = open(sys.argv[1])
    except:
        input = sys.stdin
    _dict = ""
    l,d,n = [int(i) for i in input.readline().split() if i]
    for line in range(d):
        _dict = _dict + " " + input.readline().split()[0]
    for case in range(n):
        pattern = input.readline().split()[0]
        print "Case #%d: %d" % (case+1, count_matches(pattern, _dict))
    
