#!/usr/bin/python

import sys


def solve(case):
    game, combine, reject = parse(case)
    if combine == {} and reject == {}:
        return game

    invoked = game[0]
    game = game[1:]
    for elem in game:
        pair = (invoked[-1:], elem)
        if combine.has_key(pair):
            invoked = invoked[:-1] + combine[pair]
        elif reject.has_key(elem):
            a = 1
            for e in reject[elem]:
                if e in invoked:
                    invoked = ""
                    a = 0
                    break
            if a:
                invoked += elem
        else:
            invoked += elem

    return invoked


def parse(case):
    combine = {}
    reject = {}

    i = 0
    C = int(case[i]) * 3
    i += 1
    if C > 0:
        comb = case[i]
        k = 0
        while k < C:
            combine[(comb[k], comb[k+1])] = comb[k+2]
            combine[(comb[k+1], comb[k])] = comb[k+2]
            k += 3
        i += 1

    D = int(case[i]) * 2
    i += 1
    if D > 0:
        rej = case[i]
        k = 0
        while k < D:
            a = rej[k]
            b = rej[k+1]
            if reject.has_key(a):
                reject[a].append(b)
            else:
                reject[a] = [b]
            if reject.has_key(b):
                reject[b].append(a)
            else:
                reject[b] = [a]
            k += 2
        i += 1

    N = int(case[i])
    i += 1
    game = case[i]
    return game, combine, reject


def main(data = "B-example.in"):
    f = open(data, 'r')
    inp = map(lambda x: x[:-1], f.readlines())

    T = int(inp[0])
    cases = map(lambda x: x.split(' '), inp[1:])

    i = 1
    for case in cases:
        print "Case #" + str(i) + ": [" + ", ".join(solve(case)) + "]"
        i += 1

if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print sys.argv[0] + " <input file>"
