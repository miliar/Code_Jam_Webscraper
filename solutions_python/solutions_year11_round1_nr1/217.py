#!/usr/bin/env python

import sys
import math
import random
import numpy


def solve():
    n, pd, pg = [int(x) for x in sys.stdin.readline().split()]

    ok = "True"
    if pg == 0 and pd > 0:
        ok = "False"
    elif pg == 100 and pd < 100:
        ok = "False"
    elif pd == 0:
        ok = "True"
    elif pd == 100:
        ok= "True"
    else:
        divi = 100
        if pd % 25 == 0:
            divi /= 25
        elif pd % 5 == 0:
            divi /= 5
        if pd % 4 == 0:
            divi /= 4
        elif pd % 2 == 0:
            divi /= 2
        if divi <= n:
            ok = "True"
        else:
            ok = "False"

    if ok == "True":
        return "Possible"
    else:
        return "Broken"

def run():
    CCC = int(sys.stdin.readline())
    for CC in xrange(CCC):
        print "Case #" + str(CC+1) + ": " + solve()

if __name__ == "__main__":
    run()




