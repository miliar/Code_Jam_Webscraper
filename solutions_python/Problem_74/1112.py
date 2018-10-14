from sys import stdin
#import bisect as bs
#import collections as co
#import heapq
#import itertools as it
#import math
#import re
#import string

DEBUG = True
INF = 2000000000 #2 billion
EPS = 1e-9

def line():
    return stdin.readline().strip()


def main():
    cases = int(line())
    for case in range(cases):
        parts = line().split()[1:]
        n = len(parts) / 2
        seq = [(parts[i * 2], int(parts[i * 2 + 1])) for i in range(n)]

        min_time = 0
        time_other = 0
        curr_pos = {'B': 1, 'O': 1}
        prev = 'A'

        for bot, button in seq:
            t = abs(curr_pos[bot] - button)
            if prev != bot:
                t = max(t - time_other, 0)
                time_other = 0
            t += 1
            time_other += t
            min_time += t
            curr_pos[bot] = button
            prev = bot

        print 'Case #%d: %d' % (case + 1, min_time)


if __name__ == '__main__':
    if DEBUG:
        stdin = open('input.txt')
    main()
