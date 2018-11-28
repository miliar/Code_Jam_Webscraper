import sys
import math


class Solved(Exception):
    pass


def solve(stalls, people):
    a, c = 0, 0

    while 1:
        c += 1
        a = 2 ** c
        if a > people:
            break

    result = math.floor((stalls - people) / (2 ** (c-1))) + 1
    c = math.floor(result / 2)
    d = result - c - 1

    raise Solved(
        str(max(c,d)) + ' '+ str(min(c,d))
    )

if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        try:
            solve(*list(map(int, sys.stdin.readline().strip().split(' '))))
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
