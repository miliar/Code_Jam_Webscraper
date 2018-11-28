import sys


class Solved(Exception):
    pass


def solve(cost, farm, target):
    per_second = 2.0
    total = 0.0

    while 1:
        till_end = target / per_second
        farm_time = cost / per_second

        next_per_second = (per_second + farm)
        if till_end < farm_time + (target / next_per_second):
            raise Solved(round(total + till_end, 7))
        else:
            per_second += farm
            total += farm_time


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        data = map(float, sys.stdin.readline().strip().split(' '))

        try:
            solve(*data)
        except Solved as e:
            q, w = str(e).split('.')
            w += '0'*(7-len(w))
            print('Case #{}: {}.{}'.format(i+1, q, w))
