#!/usr/bin/python

import os
import sys

DEBUG = 0 or os.getenv("DEBUG")

def debug(*what):
    if DEBUG:
        sys.stderr.write("[DEBUG] " + " ".join(map(str, what)) + "\n")

#------------------------------------------------------

def solve_case(f, R, t, r, g):
    PI = 3.1415926535897932384626
    PIdiv4 = PI / 4
    EPS = 1e-8

    g -= 2 * f
    if g < EPS:
        return 1.0
    r += f
    t += f
    R -= t 

    D = R / 2e+6 

    Rpow2 = R ** 2
    r2 = r * 2
    gr2 = g + r2
    #debug('f', f, 'R', R, 't', t, 'r', r, 'g', g)

    a = 0.0
    x = r
    while x - R < -EPS:
        debug('x', x, 'a', a)
        if (x + r) % gr2 - r2 < -EPS:
            #debug('skip string', 'x', x)
            x += r2
            continue
        else:
            Y = (Rpow2 - x ** 2) ** 0.5
            if Y - r < -EPS:
                #debug('Y < r', Y)
                break
            s = (Y + r) // gr2
            l = s * g
            y = s * gr2 + r
            if y - Y < -EPS:
                l += Y - y
            a += D * l
            #debug('x', x, 'a', a, 'l', l, 'Y', Y)
            x += D
    #debug('a', a)
    p = 1.0 - a / (PIdiv4 * (R + t) ** 2)
    if p - 0.0 < EPS:
        p = 0.0
    return p

def main():
    for case in xrange(input()):
        f, R, t, r, g = map(float, raw_input().split())
        #debug('case', case + 1, 'f', f, 'R', R, 't', t, 'r', r, 'g', g)
        print "Case #%d: %.6f" % (case + 1, solve_case(f, R, t, r, g))
main()
