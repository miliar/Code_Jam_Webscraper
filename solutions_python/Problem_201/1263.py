#!/usr/bin/python

from math import ceil, floor
import time

FREE_SEAT = ord('.')
TAKEN_SEAT = ord('O')

previous_solutions = {}

def read_input():
    cases_count = int(raw_input())
    cases = []
    for i in xrange(cases_count):
        case = map(int, raw_input().split())
        if len(case) != 2:
            raise RuntimeError('Case %s too many values' % (i,))
        cases.append(case)
    return cases

def solve(seats, users):
    if (seats, users) in previous_solutions:
        return previous_solutions[(seats, users)]

    if users == seats:
        return 0, 0

    if users == 1:
        return int(ceil((seats - 1) / 2.0)), int(floor((seats - 1) / 2.0))

    if users % 2.0 == 0:
        seats = int(ceil((seats - 1) / 2.0))
        users = int(ceil((users - 1) / 2.0))
    else:
        seats = int(floor((seats - 1) / 2.0))
        users = int(floor((users - 1) / 2.0))

    return solve(seats, users)

def calc_seat(toilet, index):
    if toilet[index] != FREE_SEAT:
        raise RuntimeError('Seat to calc isn\'t available')

    left = 0
    x = index - 1
    while toilet[x] == FREE_SEAT:
        x -= 1
    left = index - x - 1

    right = 0
    x = index + 1
    while toilet[x] == FREE_SEAT:
        x += 1
    right = x - index - 1

    return {'max': max(left, right), 'min': min(left, right)}

def select_seat(toilet):
    scores = [(i, calc_seat(toilet, i)) for i in range(1, len(toilet)-1) if toilet[i] == FREE_SEAT]
    minimal_score = max((s[1]['min'] for s in scores))
    scores = [s for s in scores if s[1]['min'] == minimal_score]
    selected_seat = max(scores, key=lambda s: s[1]['max'])
    return selected_seat

def judge(seats, users):
    toilet = bytearray()
    toilet.append(TAKEN_SEAT)
    for seat in xrange(seats):
        toilet.append(FREE_SEAT)
    toilet.append(TAKEN_SEAT)

    for user in xrange(users):
        seat = select_seat(toilet)
        toilet[seat[0]] = TAKEN_SEAT

    return seat[1]['max'], seat[1]['min']

cases = read_input()
for i, (seats, users) in enumerate(cases):
    solution = solve(seats, users)
    correct = judge(seats, users)
    if correct != solution:
        raise RuntimeError('Incorrect algorithm: %s:%s (correct: %s, calculated: %s)' % (seats, users, correct, solution,))
    print 'Case #%s: %s %s' % (i+1, solution[0], solution[1],)
