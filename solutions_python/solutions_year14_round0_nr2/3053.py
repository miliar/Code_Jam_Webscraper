#!/usr/bin/env python2.7

from sys import argv

script, filename = argv

inp = open(filename)

cases = int(inp.readline())

for num in range(0, cases):
    cookies = 0.0
    cps = 2.0
    line = inp.readline()
    line = line.rstrip('\n').split(' ')
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])

    seconds = 0.0
    while True:
        farmSeconds = C / cps
        winSeconds = X / cps
        winNextTurn = farmSeconds + (X / (cps + F))
        
        if winNextTurn < winSeconds:
            cookies = cookies - C
            cps = cps + F
            seconds = seconds + farmSeconds
        else:
            seconds = seconds + winSeconds
            print 'Case #%d: %.7f' % (num + 1, seconds)
            break
