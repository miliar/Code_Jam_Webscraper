# -*- coding: utf-8 -*-

def flip(a, left, k):
    return a[:left] + tuple((not e for e in a[left:left+k])) + a[left+k:]


def solve(s, k):
    min_steps = {}
    init = tuple((e == '+' for e in s))
    target = tuple((True for e in s))

    min_steps[init] = 0
    cur = [init]
    cont = True

    while (target not in min_steps) and cont:
        cont = False

        nxt = []
        for x in cur:
            for i in range(len(x) - k + 1):
                y = flip(x, i, k)

                if y not in min_steps:
                    cont = True
                    min_steps[y] = min_steps[x] + 1
                    nxt.append(y)

        cur = nxt

    if target not in min_steps:
        return None

    return min_steps[target]


def main():
    t = int(input())
    for i in range(t):
        s, k = input().split()
        res = solve(s, int(k))
        if res is None:
            print('Case #%d: IMPOSSIBLE' % (i + 1))
        else:
            print('Case #%d: %d' % (i + 1, res))


if __name__ == '__main__':
    main()
