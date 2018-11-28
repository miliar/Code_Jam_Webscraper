#!/usr/bin/python

import sys

MAPPING = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q'}

def generate():
    mapping = {}
    f = sys.stdin
    while True:
        googlerese, source = f.readline(), f.readline()
        if not len(googlerese):
            break
        for (x,y) in zip(source, googlerese):
            if 'a' <= x <= 'z':
                mapping[y] = x
    print mapping

def solve():
    f = sys.stdin
    T = int(f.readline().strip())
    for testid in xrange(1, T+1):
        src = f.readline().strip()
        res = ''.join(map(lambda x: 'a' <= x <= 'z' and MAPPING[x] or x, src))
        print 'Case #%s: %s' % (testid, res)

def main(argv):
    if '-generate' in argv:
        generate()
    else:
        solve()

if __name__ == '__main__':
    main(sys.argv[1:])