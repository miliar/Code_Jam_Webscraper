#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(c, f, x):
    # small: 1-500 1-4 1-2000
    # large: 1-10000 1-100 1-100000
    t = 0 #時刻
    # m = 0 #枚数
    v = 2.0 #初速

    best = x/v + 1
    k = 0
    while True: # m < x:
        dt_c = c/v
        dt_m = x/v
        # dt_c = (c - m)/v
        # dt_m = (x - m)/v
        # print "t=%g, k=%d, dt_c=%g, %g + (%g - %g)/%g = %g" % (t, k, dt_c, t, x,m,v,t+dt_m)

        t_ = t + dt_m
        if t_ >= best:
            return best
        best = t_

        t += dt_c
        # m = 0 #全部使っちゃうからね
        v += f
        k += 1

def main():
    t = input() # 1-100
    for i in range(t):
        c, f, x = map(float, raw_input().split())
        print "Case #%d: %.7f" % (1+i, solve(c,f,x))


if __name__ == '__main__':
    main()

