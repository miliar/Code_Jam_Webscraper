#!/usr/bin/env python3

import copy

neighbours = {('G', 'R'), ('R', 'Y'), ('Y', 'V'), ('R', 'B'), ('B', 'Y'), ('B', 'O')}


def solve(n, colors):
    ncolors = copy.deepcopy(colors)
    for O, S in ['BO', 'RG', 'YV']:
        if colors[O] == colors[S]:
            if n == colors[O] + colors[S]:
                return ''.join([O, S] * colors[O])
            elif colors[O] > 0:
                return 'IMPOSSIBLE'

        elif colors[O] > colors[S]:
            ncolors[O] -= colors[S]

        else:
            return 'IMPOSSIBLE'


    if ncolors['R'] > ncolors['B']:
        t = ['R', 'B']
    else:
        t = ['B', 'R']
    k = min(ncolors['R'], ncolors['B'])
    l = max(ncolors['R'], ncolors['B'])

    s = t * k
    s.extend([t[0]] * (l - k))

    r = []
    while len(s) > 0 or ncolors['Y'] > 0:
        if ncolors['Y'] > 0:
            ncolors['Y'] -= 1
            r.append('Y')
        if len(s) > 0:
            r.append(s.pop())

    while len(r) > 0:
        c = r.pop()
        s.append(c)

        if c == 'Y' and ncolors['V'] > 0:
            s.extend(['V', 'Y'] * ncolors['V'])
            ncolors['V'] = 0

        elif c == 'B' and ncolors['O'] > 0:
            s.extend(['O', 'B'] * ncolors['O'])
            ncolors['O'] = 0

        elif c == 'R' and ncolors['G'] > 0:
            s.extend(['G', 'R'] * ncolors['G'])
            ncolors['G'] = 0

    if s[0] == s[-1] and len(s) > 1:
        return 'IMPOSSIBLE'

    if len(s) != n:
        return 'IMPOSSIBLE'

    for i in range(len(s)):
        if (s[i], s[i-1]) not in neighbours and (s[i-1], s[i]) not in neighbours:
            return 'IMPOSSIBLE'

    return ''.join(s)


if __name__ == "__main__":
    t = int(input())
    for i in range(1, t + 1):
        elems = list(map(int, input().split()))
        n = elems[0]
        c = dict(zip("ROYGBV", elems[1:]))
        print("Case #{}: {}".format(i, solve(n, c)))
