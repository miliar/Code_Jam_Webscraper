import sys


class Solved(Exception):
    pass


def solve(data, l):
    l = int(l)
    data = list(data)
    counter = 0
    length = len(data)
    index = 0
    while (True):
        if index + l > length:
            break

        if data[index] == '-':
            counter += 1
            for x in range(0, l):
                data[index] = '+' if data[index] == '-' else '-'
                index += 1

        try:
            index = data.index('-')
        except ValueError:
            raise Solved(counter)

    if data == '+' * length:
        raise Solved(counter)

    raise Solved('IMPOSSIBLE')


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        try:
            solve(*sys.stdin.readline().strip().split(' '))
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
