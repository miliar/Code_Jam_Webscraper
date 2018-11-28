#!/usr/bin/env python2 -tt -Wd

def readline(line):
    i = line.index(' ')
    n = int(line[:i])
    line = line[i:].strip()
    return [int(line[j]) for j in xrange(n+1)]

def readinput():
    with open('A-large.in', 'r') as fin:
        numlines = int(next(fin))
        return [readline(next(fin)) for i in xrange(numlines)]

def solve(seq):
    total = 0
    added = 0
    for shy, num in enumerate(seq):
        if num and shy > total + added:
            added = shy-total
        total += num
    return added

def main():
    cases = readinput()
    for i, case in enumerate(cases, 1):
        print "Case #%s: %s"%(i, solve(case))

if __name__ == '__main__':
    main()
