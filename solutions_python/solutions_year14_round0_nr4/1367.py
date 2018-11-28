#!/usr/bin/env python

import sys
from copy import copy, deepcopy

def play_war(a, b):
    choose_a = max(a)
    a.remove(choose_a)

    if choose_a > max(b):
        choose_b = min(b)
        b.remove(choose_b)
        return (True, a, b)

    else:
        for i in b:
            if i > choose_a:
                b.remove(i)
                return (False, a, b)



def play_deceit(a, b):
    tell_a = None

    for i in a:
        if i > min(b):
            choose_a = i
            a.remove(choose_a)
            tell_a = max(b) + 0.0001
            break

    if tell_a == None:
        choose_a = tell_a = min(a)
        a.remove(tell_a)

    if tell_a > max(b):
        choose_b = min(b)
        b.remove(choose_b)
        return (True, a, b)

    else:
        for i in b:
            if i > tell_a:
                b.remove(i)
                return (False, a, b)

def run_case(line, content):
    N = int(content[line])
    d = 0
    w = 0

    naomi = sorted([float(i) for i in content[line+1].split()])
    ken = sorted([float(i) for i in content[line+2].split()])

    while len(naomi) > 0:
        g = play_deceit(naomi, ken)
        naomi = g[1]
        ken = g[2]
        if g[0]:
            d += 1

    naomi = sorted([float(i) for i in content[line+1].split()])
    ken = sorted([float(i) for i in content[line+2].split()])

    while len(naomi) > 0:
        g = play_war(naomi, ken)
        naomi = g[1]
        ken = g[2]
        if g[0]:
            w += 1

    return "%d %d" % (d, w)

if len(sys.argv) > 1:
    input = sys.argv[1]
else:
    input = "input.txt"

try:
    with open(input) as f:
        content = f.readlines()
except:
    print("Can not find input file: %s" % input)
    sys.exit()

T = int(content[0])

case = line = 1
while case <= T:
    line = 1 + 3 * (case-1)
    result = run_case(line, content)

    print("Case #%d: %s" % (case, result))
    case += 1
