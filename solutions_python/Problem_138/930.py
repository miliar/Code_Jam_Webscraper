#!/usr/bin/env 
import sys
import time

from pprint import pprint

# Case #1: 0 0
# Case #2: 1 0
# Case #3: 2 1
# Case #4: 8 4

def do_case(f):
    num_blocks = int(f.readline())
    naomi = sorted(map(float, f.readline().split()))
    ken = sorted(map(float, f.readline().split()))
    return play_deceitful(naomi[:], ken[:]), play_honest(naomi[:], ken[:])


def smallest_winner(values, nv):  
    if nv > max(values):
        return values.pop(0)
    i = -1
    while True:
        if values[i] > nv:
            return values.pop(i)
        i -= 1

def largest_loser(values, nv):
    """find the value of the largest loser,but don't remove it"""
    if nv > max(values):
        return values[0]
    i = -1
    while True:
        if values[i] < nv:
            return values[i]
        i -= 1
def play_honest(naomi, ken):
    np = 0
    while naomi and ken:
        nv = naomi.pop()
        kv = smallest_winner(ken, nv)
        if nv > kv:
            np += 1
    return np

def naomi_pop(naomi, ken):
    if len(naomi) == 1:
        v = naomi.pop()
        return v, v
    m, n = max(ken), min(ken)
    M, N = max(naomi), min(naomi)
    if m > M or m < N:
        v = naomi.pop(0)
        return v, v
    else: 
        v = smallest_winner(naomi, m)
        lie = largest_loser(naomi, m)
        return v, lie


def play_deceitful(naomi, ken):
    np = 0
    while naomi and ken:
        nv, lie = naomi_pop(naomi, ken)
        kv = smallest_winner(ken, lie)
        if nv > kv:
            np += 1
    return np

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    for t in xrange(1,T+1):
        print 'Case #{}: {} {}'.format(t, *do_case(f))
    f.close()

if __name__ == '__main__':
    main()    

