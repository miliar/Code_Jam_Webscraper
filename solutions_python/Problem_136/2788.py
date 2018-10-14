#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for t in range(1, T+1):
        C, F, X = list( map( float, sys.stdin.readline().split() ) )

        cookies_per_sec = 2
        min_time = X / cookies_per_sec

        time = 0
        t_new_farm = 0
        while time < min_time:
            t_new_farm = C / cookies_per_sec
            cookies_per_sec += F
            time += t_new_farm
            min_time = min(min_time, time + X / cookies_per_sec)

        print('Case #{:d}: {:.7f}'.format(t, min_time))
