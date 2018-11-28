#!/usr/bin/env python
# coding:utf-8
from __future__ import division

def process_file(file):
    fsock = open(file)
    text = fsock.read()
    fsock.close()
    lines = text.split('\n')
    return lines

def process_lines(lines):
    cases = []
    n = int(lines[0].split(' ')[0])
    for i in range(1, n+1):
        l = 3*(i-1) + 1
        m = sorted([float(x) for x in lines[l+1].split(' ')])
        n = sorted([float(x) for x in lines[l+2].split(' ')])
        cases.append((m,n))
    return cases

def process_case(case):
    m, n = case
    i, j = 0, 0
    
    while i<len(m) and j<len(n):
        while m[i] < n[j]:
            i += 1
            if i >= len(m):
                break
        if i < len(m):
            i += 1
            j += 1
    
    result0 = j

    i, j = 0, 0

    while i<len(m) and j<len(n):
        while n[j] < m[i]:
            j += 1
            if j >= len(n):
                break
        if j < len(n):
            i += 1
            j += 1

    result1 = len(m) - i
    return result0, result1
    

def main():
    import sys
    if len(sys.argv) == 1:
        filename = 'x.in'
    else:
        filename = sys.argv[1]
    lines = process_file(filename)
    cases = process_lines(lines)
    for k, v in enumerate(cases):
        case = process_case(v)
        if type(case) != type(()):
            print "Case #%d: %s" % (k + 1, case)
        else:
            print "Case #%d: %s %s" % (k + 1, case[0], case[1])

if __name__ == "__main__":
    main()