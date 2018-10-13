#!/usr/bin/pypy

import sys

# If this fails then I'm blaming it on Unstoppable, which is currently
# on Film 4 and has my attention. CHOO CHOO!!

with sys.stdin as fin:
    cases = int(fin.next())
    for i in range(cases):
        (C, F, X) = (float(d) for d in fin.next().split(' '))

        best_time = next_time = X / 2.0
        base_time = 0.0
        gen_speed = 2.0

        while True:
            base_time = base_time + C / gen_speed
            gen_speed = gen_speed + F
            next_time = base_time + (X / gen_speed)
            if next_time < best_time:
                best_time = next_time
            else:
                break

        print "Case #{}: {}".format(i+1, best_time)
