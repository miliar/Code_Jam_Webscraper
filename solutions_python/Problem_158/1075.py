#!/usr/bin/env python
# vim:fileencoding=utf-8

import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

ntest = 0
inputs = []

WIN   = "RICHARD"
LOOSE = "GABRIEL"

def solve():
    for t in range(ntest):
        x = inputs[t]["x"]
        r = inputs[t]["r"]
        c = inputs[t]["c"]

        if r * c % x != 0:
            print "Case #{0}: {1}".format(t + 1, WIN)
        elif x == 1:
            print "Case #{0}: {1}".format(t + 1, LOOSE)
        elif x == 2:
            if r * c > 1:
                print "Case #{0}: {1}".format(t + 1, LOOSE)
            else:
                print "Case #{0}: {1}".format(t + 1, WIN)
        elif x == 3:
            if r == 1 or c == 1:
                print "Case #{0}: {1}".format(t + 1, WIN)
            else:
                print "Case #{0}: {1}".format(t + 1, LOOSE)
        elif x == 4:
            if r == 1 or c == 1:
                print "Case #{0}: {1}".format(t + 1, WIN)
            elif r < 4 and c < 4:
                print "Case #{0}: {1}".format(t + 1, WIN)
            elif (r == 2 and c == 4) or (c == 2 and r == 4):
                print "Case #{0}: {1}".format(t + 1, WIN)
            else:
                print "Case #{0}: {1}".format(t + 1, LOOSE)
#             if r == 1 or c == 1:
#                 print "Case #{0}: {1}".format(t + 1, WIN)
#             elif (r == 2 and c < 4) or (c == 2 and r < 4):
#                 print "Case #{0}: {1}".format(t + 1, WIN)
#             else:
#                 print "Case #{0}: {1}".format(t + 1, LOOSE)

def parse():
    global ntest
    global inputs
    ntest = int(sys.stdin.readline().strip())
    for n in range(ntest):
        x_r_c = sys.stdin.readline().strip().split()
        x = int(x_r_c[0])
        r = int(x_r_c[1])
        c = int(x_r_c[2])
        inputs.append({"x": x, "r": r, "c": c})
    # pp.pprint(inputs)

if __name__ == '__main__':
    parse()
    solve()
