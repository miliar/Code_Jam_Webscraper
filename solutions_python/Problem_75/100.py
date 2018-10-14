#!/usr/bin/env python

import sys


def foo(line):
    words = line.split()
    c = int(words[0])
    cd = {}
    for i in range(c):
        t = words[i+1]
        cd[t[:2]] = t[2]
        cd[t[:2][::-1]] = t[2]
    words = words[c+1:]
    d = int(words[0])
    dd = {}
    for i in range(d):
        t = words[i+1]
        if t[0] not in dd:
            dd[t[0]] = set()
        if t[1] not in dd:
            dd[t[1]] = set()
        dd[t[0]].add(t[1])
        dd[t[1]].add(t[0])

    words = words[d+1:]
    n = int(words[0])
    data = words[1]
    res = []
    for x in data:
        res.append(x)
        if len(res) >= 2:
            key = ''.join(res[-2:])
            if key in cd:
                res = res[:-2] + [cd[key]]
        if res[-1] in dd:
            for x in res[:-1]:
                if x in dd[res[-1]]:
                    res = []
                    break

    res2 = '[' + ', '.join(res) + ']'
    return res2


def main(ifile, ofile):
    n = int(ifile.readline())
    for i in range(n):
        ofile.write("Case #%s: %s\n" % (i+1, foo(ifile.readline())))

main(sys.stdin, sys.stdout)

