#!/usr/bin/env python

import sys

class DoesNotExist(Exception):
    pass

def nextavail(froma, time):
    for s, e in froma:
        if s >= time:
            return (s, e)
    raise DoesNotExist

def solve(froma, fromb, turnaround):
    n_a_trains = 0
    n_b_trains = 0
    availa = -1
    availb = -1
    while len(froma) or len(fromb):
        if availa != -1 and len(froma):
            try:
                (s, e) = nextavail(froma, availa)
            except DoesNotExist:
                availa = -1
            else:
                froma.remove((s, e))
                availa = -1
                availb = e + turnaround
                continue

        if availb != -1 and len(fromb):
            try:
                (s, e) = nextavail(fromb, availb)
            except DoesNotExist:
                availb = -1
            else:
                fromb.remove((s, e))
                availb = -1
                availa = e + turnaround
                continue
        
        # pick next earliest leaving train
        if len(froma) > 0 and len(fromb) > 0:
            if froma[0] <= fromb[0]:
                availa = 0
                n_a_trains += 1
            else:
                availb = 0
                n_b_trains += 1
        elif len(froma) > 0:
            availa = 0
            n_a_trains += 1
        elif len(fromb) > 0:
            availb = 0
            n_b_trains += 1

    return (n_a_trains, n_b_trains)

def solve_problem(fname):
    l = [line.strip() for line in open(fname).readlines()]

    n_problems = int(l.pop(0))

    n = 1
    while n_problems > 0:
        turnaround = int(l.pop(0))

        n_ab = l.pop(0)
        n_a = int(n_ab.split()[0])
        n_b = int(n_ab.split()[1])

        froma = []
        for i in xrange(0, n_a):
            line = l.pop(0)
            l0 = line.split()[0]
            start = int(l0.split(':')[0]) * 60 + int(l0.split(':')[1])
            l0 = line.split()[1]
            end = int(l0.split(':')[0]) * 60 + int(l0.split(':')[1])

            froma.append((start, end))

        fromb = []
        for i in xrange(0, n_b):
            line = l.pop(0)
            l0 = line.split()[0]
            start = int(l0.split(':')[0]) * 60 + int(l0.split(':')[1])
            l0 = line.split()[1]
            end = int(l0.split(':')[0]) * 60 + int(l0.split(':')[1])

            fromb.append((start, end))

        froma.sort()
        fromb.sort()
        n_a, n_b = solve(froma, fromb, turnaround)
        print 'Case #%d: %d %d' % (n, n_a, n_b)
        n = n + 1
        n_problems = n_problems - 1

if __name__ == '__main__':
    solve_problem(sys.argv[1])
