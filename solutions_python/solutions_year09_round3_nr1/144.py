#!/usr/bin/python

import sys

def parse_tests(file):
    T = file.next()
    for alien_num in file:
       yield alien_num.strip()

DIGS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def todec(digs, base):
    mul = 1
    res = 0
    for dig in reversed(digs):
        res += dig * mul
        mul *= base
    return res

def solve(alien_num):
    adigs = list(alien_num)
    next_dig = 0
    tr = {}
    digs = []
    for adig in adigs:
        dig = tr.get(adig)
        if dig != None:
            digs.append(dig)
        elif not tr:
            tr[adig] = 1
            digs.append(1)
        else:
            tr[adig] = next_dig
            digs.append(next_dig)
            next_dig += 1
            if next_dig == 1:
                next_dig = 2

    if len(tr) <= 36:
        return int(''.join(DIGS[x] for x in digs), max(2,len(tr)))
    else:
        return todec(digs, max(2, len(tr)))

if __name__ == '__main__':
    outf = open(sys.argv[1].replace('.in','.out'), 'w')
    for i, alien_num in enumerate(parse_tests(open(sys.argv[1]))):
        print >>outf, "Case #%d: %d" % (i+1, solve(alien_num))


