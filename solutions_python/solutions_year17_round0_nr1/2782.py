#!/usr/bin/env python

def get_min_flips(pancakes, K):
    i = 0
    flips = 0
    while i <= len(pancakes) - K:
        if pancakes[i] == '-':
            new_pancakes = pancakes[:i]
            j = 0
            while j < K: 
                if pancakes[i + j] == '-':
                    new_pancakes += '+'
                else:
                    new_pancakes += '-'
                j += 1
            pancakes = new_pancakes + pancakes[i + K:]
            flips += 1
        i += 1

    while i < len(pancakes):
        if pancakes[i] == '-':
            return 'IMPOSSIBLE'
        i += 1
    return flips

if __name__ == '__main__':
    T = int(raw_input())
    for tc in range(1, T + 1):
        pancakes, K = raw_input().split()
        print 'Case #%d: %s' % (tc, get_min_flips(pancakes, int(K)))
