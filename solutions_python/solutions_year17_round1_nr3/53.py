#!/usr/bin/python

import sys

def dragon(hd_i, ad, hk, ak, b, d):
    queue = []
    visited = set()

    def take_turn(action, turn):
        if action not in visited:
            visited.add(action)
            queue.append((action, turn))

    initial = (hd_i, ad, hk, ak)

    take_turn(initial, 0)

    while len(queue) > 0:
        state, turn = queue.pop(0)

        hd, ad, hk, ak = state

        if hd > 0:
            if ad >= hk:
                return str(turn + 1)
            else:
                take_turn((hd - ak, ad, hk - ad, ak), turn + 1)
                take_turn((hd - ak, ad + b, hk, ak), turn + 1)
                take_turn((hd_i - ak, ad, hk, ak), turn + 1)

                if ak > 0:
                    ak_new = max(ak - d, 0)
                    take_turn((hd - ak_new, ad, hk, ak_new), turn + 1)

    return "IMPOSSIBLE"

num = sys.stdin.readline()

for i in range(0, int(num)):
    line = sys.stdin.readline().strip('\n')

    hd, ad, hk, ak, b, d = line.split(" ")

    hd = int(hd)
    ad = int(ad)
    hk = int(hk)
    ak = int(ak)
    b  = int(b)
    d  = int(d)

    print "Case #" + str(i + 1) + ": " + dragon(hd, ad, hk, ak, b, d)
