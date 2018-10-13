#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# google code jam - c.durr - 2017

# RollerCoasterScheduling
# https://code.google.com/codejam/contest/dashboard?c=5314486#s=p1`

from sys import stdin


def readint():
    return int(stdin.readline())

def readints():
    return list(map(int, stdin.readline().split()))

def readstring():
    return stdin.readline().strip()

def readstrings():
    return stdin.readline().split()

# def upgrade(n, tickets, r):  # r = number of trains
#     contains = [set() for _ in range(r)]
#     free = [n] * r
#     last = [n] * r
#     answer = 0
#     for p, b in tickets:
#         i = None
#         for j in range(r):
#             if b not in contains[j] and free[j] > 0:
#                 if i is None:
#                     i = j
#                 elif (last[i] < p and last[j] >= p) or ((last[i] >= p) == (last[j]) and free[i] < free[j]):
#                     i = j
#         contains[i].add(b)
#         if last[i] < p:
#             answer += 1
#         else:
#             last[i] = p - 1
#         free[i] -= 1
#     return answer

def solve(n, c, tickets):
    tickets.sort()
    trains = 1
    count = [0] * c
    seat = [0] * n
    total = 0
    for p, b in tickets:
        count[b - 1] += 1
        seat[p - 1] += 1
        total += 1
        while p * trains < total:
            trains += 1
    trains = max(trains, max(count))
    upgrade = 0
    for x in seat:
        upgrade += max(0, x - trains)
    return (trains, upgrade)


for test in range(readint()):
    n, c, m = readints()                 # read input
    tickets = [readints() for _ in range(m)]
    x, y = solve(n, c, tickets)
    print("Case #%i: %i %i"% (test+1, x, y))
