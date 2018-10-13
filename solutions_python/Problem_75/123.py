#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

def solve(line):
    line = line.split()

    combine = dict()
    C = int(line[0])
    for s in line[1:C+1]:
        combine[s[0] + s[1]] = s[2]
        combine[s[1] + s[0]] = s[2]

    opposed = set()
    D = int(line[C+1])
    for s in line[C+2:C+D+2]:
        opposed.add(s[0] + s[1])
        opposed.add(s[1] + s[0])

    invoked = line[C+D+3]
    ret = ""
    for c1 in invoked:
        if ret and ret[-1] + c1 in combine:
            ret = ret[:-1] + combine[ret[-1] + c1]
        else:
            for c2 in ret:
                if c2 + c1 in opposed:
                    ret = ""
                    break
            else:
                ret += c1

    return "[" + ", ".join(ret) + "]"


def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        ret = solve(sys.stdin.readline())
        print "Case #" + str(i+1) + ": " + str(ret)

if __name__ == '__main__':
    main()
