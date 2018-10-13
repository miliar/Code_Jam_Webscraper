#!/usr/bin/env python

def read():
    return map(float, raw_input().split())


def work(cases, (C, F, X)):
    L = 0
    R = int(X)

    
    def calc(n):
        total = 0
        spd = 2
        for i in range(n):
            total += C / spd
            spd += F
        return total + X / spd

    
    while L < R:
        LL = L +     (R - L) / 3
        RR = L + 2 * (R - L) / 3

        if calc(LL) > calc(RR):
            L = LL + 1
        else:
            R = RR

    minV = 1<<30
    for i in range(L - 3, L + 4):
        minV = min(minV, calc(i))
    
    print "Case #%d: %.10f" % (cases, minV)


if __name__ == "__main__":
    for i in range(int(raw_input())):
        work(i + 1, read())
