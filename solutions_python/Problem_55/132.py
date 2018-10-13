#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys       import stdin

# determines which group will be the first onto the next run
def get_next_run(k, G, first):
    remain = k
    ret    = 0
    for i in range(len(G)):
        remain -= G[(first + i) % len(G)]
        if remain < 0:
            ret = i
            break
        if remain == 0:
            ret = i + 1
            break
    return (first + ret) % len(G)

# start is inclusive, end is not
def sum_groups(G, start, end):
    if start < end:
        return sum(G[start:end])
    else:
        return sum(G[start:]) + sum(G[:end])

def get_head_stats(k, R, G, next, loopstart):
    idx    = 0
    runs   = 0
    riders = 0
    while idx != loopstart:
        runs   += 1
        riders += sum_groups(G, idx, next[idx])
        idx     = next[idx]
        if runs == R:
            break
    return (runs, riders)

def get_loop_stats(k, G, next, loopstart):
    idx    = loopstart
    runs   = 0
    riders = 0
    while True:
        runs   += 1
        riders += sum_groups(G, idx, next[idx])
        idx     = next[idx]
        if idx == loopstart:
            return (runs, riders)

def get_tail_stats(k, R, G, next, idx):
    riders = 0
    while R > 0:
        R      -= 1
        riders += sum_groups(G, idx, next[idx])
        idx     = next[idx]
    return riders

count = int(stdin.readline().strip())
for i in range(count):
    R, k, N = map(int, stdin.readline().strip().split())
    G       = tuple(map(int, stdin.readline().strip().split()))
    next    = [None] * len(G)

    #print("R, k, N = " + str((R, k, N)))
    #print("G    = " + str(G))

    # figure out where each load ends and the next begins
    j = 0
    while next[j] == None:
        next[j] = get_next_run(k, G, j)
        j = next[j]
    loopstart = j

    #print("next = " + str(next))

    runs, riders = get_head_stats(k, R, G, next, loopstart)
    if runs == R:
        print("Case #{0}: {1}".format(i + 1, riders))
        continue

    loopruns, loopriders = get_loop_stats(k, G, next, loopstart)
    loopcount = (R - runs) // loopruns
    runs     += loopcount * loopruns
    riders   += loopcount * loopriders
    riders   += get_tail_stats(k, R - runs, G, next, loopstart)

    print("Case #{0}: {1}".format(i + 1, riders))
