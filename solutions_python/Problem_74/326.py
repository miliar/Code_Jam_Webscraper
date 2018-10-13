#!/usr/bin/env python3

import sys

T = int(sys.stdin.readline())


for case in range(T):
    line = sys.stdin.readline().rstrip().split()
    N = int(line[0])
    bots = {
        0 : {'loc' : 1, 'spare': 0 },
        1 : {'loc' : 1, 'spare': 0 },
    }

    sum = 0
    for n in range(N):
        t_bot = line[n*2+1] == 'B'
        t_loc = int(line[n*2+2])

        r = abs(bots[t_bot]['loc'] - t_loc) 

        if r >= bots[t_bot]['spare']:
            moves = r - bots[t_bot]['spare'] + 1
        else:
            moves = 1

        bots[t_bot]['loc'] = t_loc
        bots[t_bot]['spare'] = 0
        bots[int(not t_bot)]['spare'] += moves

        sum += moves
    print('Case #{0}: {1}'.format(case+ 1, sum))
