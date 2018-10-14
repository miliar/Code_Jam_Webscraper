#!/usr/bin/python

MOD = 1000002013

import sys

def emit(text, *args):
    msg = text % args
    sys.stderr.write(msg)
    sys.stdout.write(msg)

def trip_cost(n, o, e):
    return sum(range(n, n - (e - o), -1))

def solve(n, arr):
    true_cost = 0
    false_cost = 0
    entrants = [0] * n
    exits = [0] * n
    for (o, e, p) in arr:
        entrants[o - 1] += p
        exits[e - 1] += p
        true_cost += p * trip_cost(n, o, e)
    tickets = [0] * n
    for i in range(n):
        tickets[i] = entrants[i]
        leaving = exits[i]
        for swapnr in range(i, -1, -1):
            leaving_with = min(tickets[swapnr], leaving)
            false_cost += leaving_with * trip_cost(n, swapnr, i)
            tickets[swapnr] -= leaving_with
            leaving -= leaving_with
            if leaving == 0:
                break
    return (true_cost - false_cost) % MOD

def getline():
    return sys.stdin.readline().rstrip('\n')

ncases = int(getline())

for casenr in range(1, ncases+1):
    n, m = [ int(s) for s in getline().split() ]
    arr = [ [ int(s) for s in getline().split() ]
            for i in range(m) ]
    emit("Case #%d: %s\n", casenr, solve(n, arr))
