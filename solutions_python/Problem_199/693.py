#!/usr/bin/python3

def check(state, size):
    ret = 0
    state = list(state)
    for i in range(len(state)):
        if state[i] == '-':
            ret += 1
            for j in range(i, i+size):
                state[j] = '-' if state[j] == '+' else '+'
    return ret

if __name__ == '__main__':
    N = int(input())
    for case in range(1, N+1):
        line = input().split(' ')
        try:
            res = check(line[0], int(line[1]))
            print("Case #%d: %d"%(case, res))

        except(IndexError):
            print("Case #%d: IMPOSSIBLE"%case)
