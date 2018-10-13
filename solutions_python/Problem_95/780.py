#!/usr/bin/env python

import sys
import string

lookup = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
lookup['q'] = 'z'
lookup['z'] = 'q'

def samples():
    f = open('a.sample', 'r')
    for l in string.lowercase:
        try:
            lookup[l]
        except:
            print "key not found:", l
    letters = [v for k,v in lookup.iteritems()]
    missing = [x for x in string.lowercase if x not in letters]

def main():
    f = open(sys.argv[1], 'r')
    lines = f.readline()
    for l in xrange(int(lines)):
        line = f.readline().strip()
        plain = ''
        for i in xrange(len(line)):
            plain += lookup[line[i]]
        print "Case #%i: %s" % (l+1, plain)

if __name__ == '__main__':
    samples()
    main()

