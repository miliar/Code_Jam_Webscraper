#! /usr/bin/env python -u
# coding=utf-8
import sys

__author__ = 'xl'

if __name__ == "__main__":
    fp = open("B.in")
    sys.stdout = open("B.out", "w")
    # fp = sys.stdin
    T = int(fp.readline())
    for t in range(T):
        c, f, x = map(float, fp.readline().split())

        time = 0
        rate = 2.0
        while (True):
            app1 = x / rate
            app2 = c / rate + x / (rate+f)
            if app1 <= app2:
                time += app1
                break
            else:
                time += c / rate
                rate += f

        print "Case #%s: %0.7f" % (t + 1, time)



