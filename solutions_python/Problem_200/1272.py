#!/usr/bin/env python3
# coding=utf-8


def _back_propagate_sub(nlist):
    nlist[-1] -= 1
    if len(nlist) == 1:
        return nlist

    if nlist[-2] <= nlist[-1] and nlist[-1] >= 0:
        return nlist
    else:
        return _back_propagate_sub(nlist[:-1]) + [9]


def _combine(nlist):
    slist = [str(x) for x in nlist]
    return int(''.join(slist))


def prev_tidy(n):
    nlist = [int(x) for x in str(n)]
    res = nlist
    prev_digit = 0
    for i, x in enumerate(nlist):
        if x < prev_digit:
            res = _back_propagate_sub(nlist[0:i+1]) + [9] * (len(nlist) - i - 1)
            break
        else:
            prev_digit = x

    return int(_combine(res))

if __name__ == '__main__':
    file = 'B-large'
    with open(file+'.in', 'r') as inp:
        lines = inp.readlines()

    T = int(lines[0])
    with open(file+'.out', 'w') as out:
        for i in range(1, T + 1):
            n = int(lines[i])
            res = prev_tidy(n)
            out.write('Case #%d: %d\n' % (i, res))