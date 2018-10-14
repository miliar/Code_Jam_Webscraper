import sys


class Solved(Exception):
    pass


def solve(_max, data):
    amount = 0
    s = 0

    for i, item in enumerate(data):
        add = 0
        if i > s:
            add = i - s

        amount += add
        s += item + add

    raise Solved(amount)


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        _max, data = sys.stdin.readline().strip().split(' ')
        _max = int(_max)
        data = list(map(int, list(data)))

        try:
            solve(_max, data)
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
