#!/usr/local/bin/python

import sys

def flip(s, n, i):
    return tuple( not s[j] if i <= j and j < i + n else s[j] for j in range(len(s)) )


def answer(initial, n):
    l = len(initial)
    maxflip = l - (n - 1)
    worklist = [initial]
    states = { initial: 0 }

    while worklist:
        state = worklist.pop(0)
        flips = states[state]
        #print state
        if all(state):
            return flips
        
        for i in range(maxflip):
            newstate = flip(state, n, i)

            if newstate not in states:
                states[newstate] = flips + 1
                worklist.append(newstate)
        
    return 'IMPOSSIBLE'


def solve():
    with open(sys.argv[1]) as f:
        f.readline()
        i = 1
        for line in f:
            parts = line.strip().split(' ')
            
            n = int(parts[1])
            ps = tuple( c == '+' for c in parts[0] )
            result = answer(ps, n)
            
            print('Case #{}: {}'.format(i, result))
            i = i + 1


solve()
