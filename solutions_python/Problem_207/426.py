import sys
import random


class Solved(Exception):
    pass


def choose(data, key, allowed):
    s = 0
    K = None
    for _ in allowed[key]:
        if s < data[_]:
            s = data[_]
            K = _

    return K


def solve(L, R, O, Y, G, B, V):
    out = []
    N = {
        'R': ['B', 'Y', 'G'],
        'G': ['R'],
        'B': ['Y', 'R', 'O'],
        'O': ['B'],
        'Y': ['R', 'B', 'V'],
        'V': ['Y']
    }
    H = {'R': R, 'O': O, 'Y': Y, 'G': G, 'B': B, 'V': V}

    c = random.choice(list(k for k, v in H.items() if v > 0))
    H[c] -= 1
    out.append(c)
    while sum(H.values()):
        try:
            c = random.choice(choose(H, c, N))
        except TypeError:
            raise Solved('IMPOSSIBLE')

        H[c] -= 1
        out.append(c)

    if out[0] not in N[out[-1]]:
        if out[-1] in N[out[-3]]:
            out[-1], out[-2] = out[-2], out[-1]

    if out[0] not in N[out[-1]]:
        raise Solved('IMPOSSIBLE')

    raise Solved(''.join(out))


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        try:
            solve(*list(map(int, sys.stdin.readline().split(' '))))
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
