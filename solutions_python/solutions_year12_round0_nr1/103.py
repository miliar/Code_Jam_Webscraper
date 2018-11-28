#!/usr/bin/python

import os
import sys

fin = sys.stdin

M = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def translate(c):
    ret = ''
    for i in c:
        ret += M[i]
    return ret

def main():
    T = int(fin.readline())
    for t in xrange(1, T + 1):
        l = fin.readline().strip()
        print 'Case #%d: %s' % (t, translate(l))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = open(sys.argv[1], 'r')
    main()
