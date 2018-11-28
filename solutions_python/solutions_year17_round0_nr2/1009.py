import sys


class Solved(Exception):
    pass


def solve(data):
    data = int(data)
    if data < 10:
        raise Solved(data)

    s = str(data)[::-1]
    for j in range(0, len(s)-1):
        try:
            a, b = int(s[j]), int(s[j+1])
            if a == 0 or a < b:
                data = data // (10**(j+1)) * (10**(j+1)) - 1
                s = str(data)[::-1]
        except IndexError:
            break

    raise Solved(data)


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        try:
            solve(sys.stdin.readline().strip())
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
