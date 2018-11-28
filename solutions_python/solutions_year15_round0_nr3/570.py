#! /usr/bin/env python3

import sys
from functools import reduce
from itertools import count

TABLE = \
{
    "1": {
        "1": "-1",
        "i": "i",
        "j": "j",
        "k": "k",
    },
    "i": {
        "1": "i",
        "i": "-1",
        "j": "k",
        "k": "-j",
    },
    "j": {
        "1": "j",
        "i": "-k",
        "j": "-1",
        "k": "i",
    },
    "k": {
        "1": "k",
        "i": "j",
        "j": "-i",
        "k": "-1",
    },

    "-1": {
        "1": "1",
        "i": "-i",
        "j": "-j",
        "k": "-k",
    },
    "-i": {
        "1": "-i",
        "i": "1",
        "j": "-k",
        "k": "j",
    },
    "-j": {
        "1": "-j",
        "i": "k",
        "j": "1",
        "k": "-i",
    },
    "-k": {
        "1": "-k",
        "i": "-j",
        "j": "i",
        "k": "1",
    },
}

NEXT = \
{
    "i": "j",
    "j": "k",
    "k": None,
}

def mult(a, b):
    return TABLE[a][b]

def solve(inp, times):
    if len(inp) * times < 3:
        return False

    inp = inp * times
    prg = [["1", "i", ""]]

    for i, c in enumerate(inp):
        nxt = []

        for p in prg:
            nc = mult(p[0], c)
            tdd = [nc, p[1]]
            if not tdd in nxt:
                nxt.append(tdd)

            if nc == p[1]:
                if NEXT[p[1]] != None:
                    tdd = ["1", NEXT[p[1]]]#, p[2] + c + " "]
                    if not tdd in nxt:
                        nxt.append(tdd)
                elif i == len(inp) - 1:
                    return True

        prg = nxt

    return False

with open(sys.argv[1]) as f:
    lines = f.readlines()[1:]
    lines.reverse()
    for i in count():
        if not lines:
            break
        times = int(lines.pop().split()[1])
        inp = lines.pop()[:-1]

        res = solve(inp, times)
        print("Case #%d: %s" % (i + 1, "YES" if res else "NO"))
