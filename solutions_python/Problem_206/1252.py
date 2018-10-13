#!/usr/bin/env python
def solve():
    #print "D = %d, N = %d" % (D, N)
    max_time = 0
    for h in horses:
        K = h[0]
        S = h[1]
        #print "K = %d, S = %d" % (K, S)
        t = (D - K) / float(S)
        if t > max_time :
            max_time = t

    return D / max_time

T = input()
for i in range(1, T + 1):
    fields = raw_input().split()
    D = int(fields[0])
    N = int(fields[1])
    horses = []
    for j in range(1, N + 1):
        horse_fields = raw_input().split()
        K = int(horse_fields[0])
        S = int(horse_fields[1])

        horses.append((K, S))

    max_speed = solve()
    print "Case #%d: %f" % (i, max_speed)
