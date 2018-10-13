#!/usr/bin/env python

"""
Google Code Jam 2009 - Qualification round
Alien Language
"""

import sys

def read_from(fh, num):
    return [fh.readline() for i in xrange(num)]

def add_all_prefs(ln, D):
    for i in range(len(ln)):
        D[ln[:i+1]] = 1

def calc_res(prefix, term, D):
    if not term:
        return int(D.has_key(prefix))
    if prefix and not D.has_key(prefix):
        return 0
    else:
        if term[0] == '(':
            total = 0
            choices, sep, rest = term[1:].partition(')')
            for i in choices:
                total += calc_res(prefix + i, rest, D)
            return total
        else:
            return calc_res(prefix + term[0], term[1:], D)

def main(args):
    if len(args) < 2:
        return 1
    try:
        f = open(args[1])
        #READ appropriate args from initial lines
        L, D, N = [int(x) for x in f.readline().split()]

        #build prefix word dictionary
        word_prefs = {}
        for w in range(D):
            add_all_prefs(f.readline().rstrip(), word_prefs)

        #read in and calculate solution for each input
        for case in range(N):
            print "Case #%d: %d" % (case+1, 
                   calc_res("", f.readline().rstrip(), word_prefs))
    except IOError:
        print "Invalid file input"
        return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
