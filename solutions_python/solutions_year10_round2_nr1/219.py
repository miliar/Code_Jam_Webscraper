#!/usr/bin/env python

import re, sys

def mkdirs(existing, newdir):
    compons = newdir.split('/')[1:]
    fp = ''
    c = 0
    for i in xrange(len(compons)):
        fp += '/' + compons[i]
        if not existing.has_key(fp):
            existing[fp] = True
            c += 1
    return c

def solve(existing, needed):
    dirs = {'/':True}
    for d in existing:
        dirs[d.strip()] = True
    
    t = 0
    for d in needed:
        t += mkdirs(dirs, d.strip())

    return t

def main():
    lines = sys.stdin.readlines()
    T = int(lines[0])
    
    case = 1
    i = 1
    while True:
        N, M = lines[i].split(' ')
        N, M = int(N), int(M)
        i += 1
        existing = lines[i:i+N]
        i += N
        needed = lines[i:i+M]
        i += M
        output = solve(existing, needed)
        print 'Case #%d: %s' % (case, output)
        if case == T:
            return
        case += 1

if __name__ == '__main__': main()
