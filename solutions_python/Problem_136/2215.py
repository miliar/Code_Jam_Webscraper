#! /usr/bin/env python
from sys import argv, maxint, exit

argc = len(argv)
if (argc < 2):
    print "NO FILE ARG"
    exit(1)

f = open(argv[1],'r')

T = int(f.readline())


for j in range(1,T+1):
    C,F,X = map(float,f.readline().split(' '))

    r = 2.0
    cur_min = maxint
    prev = maxint
    hard_ass_prev = 0.0

    acc = 0.0
    i = True
    while True:
        time_if_lazy = X / r
        time_to_C = C / r
        r += F

        time_if_hardass = time_to_C + (X/r) + acc
        if (time_if_lazy < time_if_hardass and i):
            print("Case #%d: %.7f" % (j,time_if_lazy))
            break
        if (time_if_hardass > prev):
            print("Case #%d: %.7f" % (j,prev))
            break
        acc += time_to_C
        prev = time_if_hardass
        i = False
