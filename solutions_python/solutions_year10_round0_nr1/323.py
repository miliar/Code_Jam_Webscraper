#!/usr/bin/env python3
#

def snap(N, K):
    state = '{:0{}b}'.format(K, N)
    if state.endswith('1' * N):
        return 'ON'
    else:
        return 'OFF'


if __name__ == '__main__':
    try:
        input()     # don't care about number of cases
        case = 1
        while True:
            N, K = map(int, input().split())
            print('Case #{}: {}'.format(case, snap(N, K)))
            case += 1
    except EOFError:
        pass
