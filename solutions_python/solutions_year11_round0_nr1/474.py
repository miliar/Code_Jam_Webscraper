#!/usr/bin/env python

import sys

if __name__ == "__main__":
    T = input()
    for t in range(T):
        data = iter(sys.stdin.readline().split())
        N = int(data.next())

        bot = "OB"
        pos = [1,1]
        ready = [0,0]
        r = 0
        for n in range(N):
            i = bot.find(data.next())
            assert i >= 0
            p = int(data.next())

            ready[i] += abs(pos[i]-p)+1
            r = ready[i] = max(r+1, ready[i])
            pos[i] = p
            # print '{} {} {}'.format(bot[i], pos[i], ready[i])

        print "Case #{}: {}".format(t+1, r)

