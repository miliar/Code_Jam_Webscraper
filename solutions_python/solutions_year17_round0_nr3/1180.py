#! /usr/bin/env python3

from collections import Counter

def solve(N, K):
    dist = Counter({N : 1})
    while K > 0:
        current_max = max(dist)
        assert current_max > 0
        number = dist[current_max]
        del dist[current_max]
        K -= number
        if current_max % 2 == 0:
            min_dist = current_max//2 - 1
            max_dist = current_max//2
        else:
            min_dist = max_dist = current_max//2
        dist[min_dist] += number
        dist[max_dist] += number
    return max_dist, min_dist

if __name__ == '__main__':
    T = int(input())
    for case in range(T):
        N, K = (int(n) for n in input().split())
        max_dist, min_dist = solve(N, K)
        print('Case #%d: %d %d' % (case+1, max_dist, min_dist))
