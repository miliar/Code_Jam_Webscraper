#!/usr/bin/env python3

FILE = "B-large.in"

def gen():
    with open(FILE) as f:
        for case in range(1, int(f.readline())+1):
            C, F, X = list(map(float, f.readline().split()))
            yield case, C, F, X


with open("cookieclickeroutputlarge.txt", "w") as out:
    for case, C, F, X in gen():
        rate = 2.0
        time = 0.0
        while True:
            farmtime = C / rate
            xtime = X / rate
            if farmtime + X / (rate + F) < xtime:
                rate += F
                time += farmtime
            else:
                time += xtime
                break
        print("Case #{0}: {1}".format(case, time), file=out)
