#!/usr/bin/python3

import re

def recurse(state, curr_city, curr_e, curr_s, curr_time, N, E, S, distants):
    if curr_city == N - 1:
        state['best'] = min(state['best'], curr_time)
        return

    if curr_e >= distants[curr_city]:
        recurse(state, curr_city + 1, curr_e - distants[curr_city], curr_s, curr_time + distants[curr_city] / curr_s, N, E, S, distants)

    if E[curr_city] >= distants[curr_city]:
        recurse(state, curr_city + 1, E[curr_city] - distants[curr_city], S[curr_city], curr_time + distants[curr_city] / S[curr_city], N, E, S, distants)

def solve(N, Q, E, S, grid, pairs):
    if Q > 1:
        return 0

    distants = []
    for i in range(N - 1):
        distants.append(grid[i][i + 1])

    state = {
        'best': float('inf')
    }
    recurse(state, 1, E[0] - distants[0], S[0], distants[0] / S[0], N, E, S, distants)

    return state['best']

def main():
    T = int(input())

    for idx in range(T):
        line = input()
        tokens = re.split(' ', line)
        N = int(tokens[0])
        Q = int(tokens[1])

        E = []
        S = []
        for i in range(N):
            line = input()
            tokens = re.split(' ', line)
            E.append(int(tokens[0]))
            S.append(int(tokens[1]))

        grid = []
        for i in range(N):
            line = input()
            tokens = re.split(' ', line)
            grid.append([int(token) for token in tokens])

        pairs = []
        for i in range(Q):
            line = input()
            tokens = re.split(' ', line)
            pairs.append([int(token) for token in tokens])

        result = solve(N, Q, E, S, grid, pairs)

        print('Case #{}: {}'.format(idx + 1, '%.6f' % result))

if __name__ == '__main__':
    main()
