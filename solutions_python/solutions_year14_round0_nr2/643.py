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
        line = lines[i].split(' ')
        cases.append(line)
    return cases

def process_case(case):
    c, f, x = [float(x) for x in case]
    inc = 2
    m = x/inc

    t0 = c/inc
    inc += f
    t = t0 + x/inc
    while (t <= m):
        m = t
        t0 += c/inc
        inc += f
        t = t0 + x/inc
    return m

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