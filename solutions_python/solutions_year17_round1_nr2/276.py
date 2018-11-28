#!/usr/bin/env pypy

import sys


def read(lines):
    ##print lines
    ins, ps = lines[0].split()
    ins = int(ins)
    ps = int(ps)
    reqs = map(int, lines[1].split())
    assert len(reqs) == ins
    insx = [map(int, l.split()) for l in lines[2:2 + ins]]
    #for i in range(ins):
    #    for j, n in enumerate(lines[2 + i].split()):
    #        pas[i][j] = int(n)
    return (reqs, insx), lines[2 + ins:]


c = 0

def rec(case, xia):
    reqs, pas = case

    if not reqs:
        #print 'done'
        return 1

    req = reqs[0]
    pa = pas[0]

    global c
    c += 1
    #print '--- %d IN ---' % c

    n = 0
    #print pa, req
    if xia is None:
        for p in pa:
            ia = int(p / req)
            #print 'try', p, req, ia
            f = 0
            mr = None
            while True:
                #print 'f-', f
                if (req * (ia + f) * 0.9 <= p <= req * (ia + f) * 1.1):
                    #print 'fia', ia + f, 'is good'
                    r = rec((reqs[1:], pas[1:]), ia + f)
                    if r > mr or mr is None:
                        #print 'NEW MR: %d' % r
                        mr = r
                    f -= 1
                else:
                    break
            f = 1
            while True:
                #print 'f+', f
                if (req * (ia + f) * 0.9 <= p <= req * (ia + f) * 1.1):
                    #print 'fia', ia + f, 'is good'
                    r = rec((reqs[1:], pas[1:]), ia + f)
                    if r > mr or mr is None:
                        #print 'NEW MR: %d' % r
                        mr = r
                    f += 1
                else:
                    break
            if mr is not None:
                #print 'ADDING: %d' % mr
                n += mr
    else:
        mr = None
        for p in pa:
            if (req * xia * 0.9 <= p <= req * xia * 1.1):
                #print 'xia', xia, 'is good'
                r = rec((reqs[1:], pas[1:]), xia)
                if r > mr or mr is None:
                    mr = r
        if mr is not None:
            n += mr

    #print '--- %d OUT: %d ---' % (c, n)
    c -= 1

    return n


def go(case):
    #print "=====", case
    global c
    c = 0
    return str(rec(case, None))


def main():
    lines = sys.stdin.read().splitlines()

    cases = int(lines[0])
    lines = lines[1:]

    for i in range(cases):
        assert lines
        case, lines = read(lines)
        print 'Case #%d: %s' % (i + 1, go(case))

    assert not lines


if __name__ == '__main__':
    main()
