'''
Created on Sep 13, 2009

@author: psyho
'''

from itertools import permutations

def num_released_after(P, released, n):
    next_released = P
    for r in released:
        if r > n and r < next_released:
            next_released = r
    return next_released-n-1

def num_released_before(P, released, n):
    next_released = -1
    for r in released:
        if r < n and r > next_released:
            next_released = r
    return n-next_released-1

def gold_needed(P, prisoners, min_so_far):
    prison = [1] * P
    gold = 0
    released = []
    for prisoner in prisoners:
        if gold > min_so_far: return ()
        prison[prisoner] = 0
        released.append(prisoner)
        n = prisoner - 1
        gold += num_released_after(P, released, prisoner)
        gold += num_released_before(P, released, prisoner)
    return gold

def min_gold_needed(P, to_release):
    min = () #inf
    for p in permutations(to_release):
        gold = gold_needed(P, p, min)
        if gold < min: min = gold
    return min

def main():
    T = int(raw_input())
    for i in xrange(T):
        P, Q = map(int, raw_input().split())
        to_release = map(int, raw_input().split())
        to_release = [x-1 for x in to_release]
        print 'Case #%d: %d' % (i+1, min_gold_needed(P, to_release))

if __name__ == '__main__':
    main()