#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

STALLS = None
LS = None
RS = None

def choose(N):
    global STALLS
    global LS
    global RS

    maximal_min_val = -1
    maximal_min_idx = list()
    for n in range(N+2):
        if 1 == STALLS[n]:
            continue
        t_m = min(LS[n], RS[n])
        if maximal_min_val > t_m:
            continue
        elif maximal_min_val == t_m:
            maximal_min_idx.append(n)
            continue
        else:
            # maximal_min_val < t_m
            maximal_min_val = t_m
            maximal_min_idx = [n, ]

    max_val = max(LS[maximal_min_idx[0]], RS[maximal_min_idx[0]])
    max_idx = [maximal_min_idx[0], ]
    for i in range(1, len(maximal_min_idx), 1):
        t_m = max(LS[maximal_min_idx[i]], RS[maximal_min_idx[i]])
        if max_val > t_m:
            continue
        elif max_val == t_m:
            max_idx.append(maximal_min_idx[i])
        else:
            # max_val < t_m
            max_val = t_m
            max_idx = [maximal_min_idx[i], ]

    return max_idx[0]

def enter(idx):
    STALLS[idx] = 1

    # update right(left space table)
    LS[idx] = -1
    dist = 0
    while STALLS[idx+1+dist] != 1:
        LS[idx+1+dist] = dist
        dist += 1

    # update left(right space table)
    RS[idx] = -1
    dist = 0
    while STALLS[idx - 1 - dist] != 1:
        RS[idx - 1 - dist] = dist
        dist += 1

def solve(cipher):
    global STALLS
    global LS
    global RS

    N, K = cipher.split(" ")
    N = int(N)
    K = int(K)

    STALLS = [0,]*(N+2)
    STALLS[0] = 1
    STALLS[-1] = 1

    LS = list()
    val = -1
    for i in range(N+2):
        LS.append(val)
        val += 1
    LS[-1] = -1
    RS = list()
    for i in range(N+2):
        val -= 1
        RS.append(val)
    RS[0] = -1

    max_val = -1
    min_val = -1
    for k in range(K):
        i = choose(N)
        max_val = max(LS[i], RS[i])
        min_val = min(LS[i], RS[i])
        enter(i)
    return "%d %d"%(max_val, min_val)

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
