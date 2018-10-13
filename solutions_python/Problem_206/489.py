import sys


class Solved(Exception):
    pass


def solve(d, horses):
    s = 0
    for h in horses:
        p = (d - h[0]) / h[1]
        s = max(p, s)

    raise Solved(round(d / s, 6))


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        try:
            d, total = list(map(int, sys.stdin.readline().split(' ')))
            h = []
            for _ in range(total):
                h.append(list(map(int, sys.stdin.readline().split(' '))))
            solve(d, h)
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
