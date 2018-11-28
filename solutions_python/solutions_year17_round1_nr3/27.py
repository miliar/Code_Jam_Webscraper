# coding: utf8

import sys

import numpy


def main():
    T = int(sys.stdin.readline())
    for _T in range(T):
        Hd, Ad, Hk, Ak, B, D = list(map(int, sys.stdin.readline().split()))
        # state: Hd, Ad (<=Hk), Hk, Ak(>=0) value: min move
        min_moves = numpy.zeros((Hd + 1, Hk + 1, Hk + 1, Ak + 1), dtype=numpy.int)
        INF = 10000
        min_moves.fill(INF)
        min_moves[Hd, Ad, Hk, Ak] = 0
        moves = {
            'heal': lambda x: [Hd] + x[1:],
            'attack': lambda x: [x[0], x[1], max(x[2] - x[1], 0), x[3]],
            'buff': lambda x: [x[0], min(x[1] + B, x[2]), x[2], x[3]],
            'debuff': lambda x: [x[0], x[1], x[2], max(x[3] - D, 0)],
        }
        attacked = lambda x: [max(x[0] - x[3], 0)] + x[1:]
        states = [[Hd, Ad, Hk, Ak]]
        while states:
            next_states = set()
            for state in states:
                tmp_moves = []
                if state[0] < Hd:
                    tmp_moves.append(moves['heal'])
                tmp_moves.append(moves['attack'])
                if state[1] < state[2]:
                    tmp_moves.append(moves['buff'])
                if state[3] > 0:
                    tmp_moves.append(moves['debuff'])
                for move in tmp_moves:
                    new_state = move(list(state))
                    if new_state[2] > 0:
                        new_state = attacked(new_state)
                    if min_moves[state[0], state[1], state[2], state[3]] + 1 < min_moves[new_state[0], new_state[1], new_state[2], new_state[3]]:
                        min_moves[new_state[0], new_state[1], new_state[2], new_state[3]] = min_moves[state[0], state[1], state[2], state[3]] + 1
                        if new_state[2] > 0 and new_state[0] > 0:
                            next_states.add(tuple(new_state))
            states = next_states
            #print(list(states))
        result = min_moves[:,:,0,:].min()
        if result == INF:
            result = 'IMPOSSIBLE'
        print('Case #%s: %s' % (_T + 1, result))


if __name__ == '__main__':
    main()
