#!/usr/bin/env python

import sys


def foo(line):
    words = line.split()
    n = int(words[0])
    
    res = 0
    d = {'O': [1, 0],
            'B': [1, 0]}
    for i in range(n):
        k = words[i*2+1]
        v = int(words[i*2+2])
        data = d[k]
        dt = abs(v - data[0])+1
        res = max(res+1, data[1]+dt)
        d[k] = [v, res]
    return res


def main(ifile, ofile):
    n = int(ifile.readline())
    for i in range(n):
        ofile.write("Case #%s: %s\n" % (i+1, foo(ifile.readline())))

main(sys.stdin, sys.stdout)

