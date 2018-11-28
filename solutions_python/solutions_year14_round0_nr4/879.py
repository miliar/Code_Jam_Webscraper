import sys
import bisect


class Solved(Exception):
    pass


def solve(a, b):
    a.sort()
    b.sort()
    x, y = a.copy(), b.copy()
    score1, score2 = 0, 0

    while a:
        v = a[0]
        i = bisect.bisect_left(b, v)
        if i == len(b) or len(b) == 1:
            found = b[0]
        else:
            found = b[i]

        if v > found:
            score2 += 1

        a.remove(v)
        b.remove(found)


    a, b = x, y
    while a:
        if a[-1] > b[-1]:
            v = a[-1]
            i = bisect.bisect_left(b, b[-1] - 0.00000001)
        else:
            v = a[0]
            i = bisect.bisect_left(b, b[-1] - 0.00000001)

        if i == len(b) or len(b) == 1:
            found = b[0]
        else:
            found = b[i]

        if v > found:
            score1 += 1

        a.remove(v)
        b.remove(found)

    raise Solved('{} {}'.format(score1, score2))


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        sys.stdin.readline()
        data = [
            list(map(float, sys.stdin.readline().strip().split(' '))),
            list(map(float, sys.stdin.readline().strip().split(' '))),
        ]
        try:
            solve(*data)
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
