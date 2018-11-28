#!/usr/bin/env python3

# Solution to problem B: Magicka (easy/hard)
# Written in Python 2/3 (http://www.python.org/)

def solve(C, D, I):

    combines = {}
    for a,b,c in C:
        combines [a,b] = combines [b,a] = c

    opposes = {}
    for a,b in D:
        opposes[a,b] = opposes[b,a] = True

    L = []
    for c in I:

        # First, try to combine with last element in the lest:
        if L != []:
            d = L[-1]
            if (c,d) in combines:
                L[-1] = combines[c,d]
                continue

        # Second, search for an opposite element:
        for d in L:
            if (c,d) in opposes:
                L = []
                break
        else:
            # Finally, if nothing else happened, just add it to the list:
            L.append(c)

    return L

if __name__ == '__main__':
    from sys import stdin
    T = int(stdin.readline())
    for t in range(1, T + 1):
        input = stdin.readline().split()
        C = int(input[0])
        D = int(input[C+1])
        N = int(input[C+1+D+1])
        answer = solve(input[1:C+1], input[C+2:C+1+D+1], input[C+1+D+2])
        print('Case #' + str(t) + ': [' + ', '.join(answer) + ']')
