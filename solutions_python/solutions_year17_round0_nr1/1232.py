#! /usr/bin/python

P_UP = ord('+')
P_DOWN = ord('-')

def read_input():
    cases = []
    cases_count = int(raw_input())
    for i in xrange(cases_count):
        case = raw_input().split()
        cases.append((case[0], int(case[1])))
    return cases

def flip(pancake):
    if pancake == P_UP:
        return P_DOWN
    return P_UP

def solve(pan, flipper):
    flips = 0
    pan = bytearray(pan)
    for i in xrange(len(pan)):
        pancake = pan[i]
        if pancake == P_DOWN:
            if i + flipper > len(pan):
                return 'IMPOSSIBLE'
            flips += 1
            for j in xrange(i, i+flipper):
                pan[j] = flip(pan[j])
    return flips

def solve_negative(pan, flipper):
    flips = 0
    pan = bytearray(pan)
    for i in xrange(len(pan)-1, -1, -1):
        pancake = pan[i]
        if pancake == P_DOWN:
            if i - flipper + 1 < 0:
                return 'IMPOSSIBLE'
            flips += 1
            for j in xrange(i, i-flipper, -1):
                pan[j] = flip(pan[j])
    return flips

cases = read_input()
for i, case in enumerate(cases):
    solution = solve(*case)
    negative_solution = solve_negative(*case)
    if solution != negative_solution:
        raise RuntimeError('Invalid Algorithm')
    print 'Case #%s: %s' % (i+1, solution,)
