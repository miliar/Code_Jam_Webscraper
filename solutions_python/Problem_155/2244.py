#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys


def friends_needed(c):
    friends = 0
    standing = c[0]
    for si in range(1, len(c)):
        if standing >= si:
            standing += c[si]
        else:
            remaining = si - standing
            friends += remaining
            standing += remaining + c[si]
    return friends


def main():
    t = int(sys.stdin.readline())
    for i in range(1, t + 1):
        line = sys.stdin.readline()
        audience_string = line.split()[1]
        c = map(int, list(audience_string))
        result = friends_needed(c)
        print "Case #{0}: {1}".format(i, result)


if __name__ == '__main__':
    main()
