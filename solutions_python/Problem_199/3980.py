#!/usr/bin/env python
import copy, itertools
lines_per_case = 1

def impossible (pl, f):
    l = len(pl)
    if f > l/2:
        slice = pl[l-f:f]
        if sum (slice) not in [0,len(slice)]:
            return True
    return False

def is_completed (pl):
    for p in pl:
        if not p:
            return False
    return True

def flip (l,i,f):
    for v in xrange(i,i+f):
        l[v] = not l[v]

def try_tuple (l,f,t):
    for i in t:
        flip (l,i,f)
    return is_completed(l)

def get_move_count (pancakelist,flipper):
    if impossible(pancakelist,flipper):
        return 'IMPOSSIBLE'
    flippingpos = range (0, len(pancakelist)-flipper+1)

    if is_completed(pancakelist):
        return '0'
    for i in xrange (0,len(pancakelist)):
        for t in itertools.combinations(flippingpos,i+1):
            if try_tuple(copy.copy(pancakelist),flipper,t):
                return str(i+1)
    return 'IMPOSSIBLE'

def stobool (c):
    if c == '+':
        return True
    else:
        return False

def process_case (line):
    p, f = line.split(' ')
    pl = [stobool(c) for c in p]
    return get_move_count(pl, int(f))



case_count = int (raw_input())
for i in xrange (case_count):
    if lines_per_case == 1:
     case = raw_input()
    else:
        case = []
        for j in xrange (lines_per_case):
            case.append(raw_input())
    print ('Case #' + str(i+1) + ': ' + process_case(case))