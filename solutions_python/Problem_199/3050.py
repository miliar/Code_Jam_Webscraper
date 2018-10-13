# -*- coding: utf-8 -*-

CAKES = {
    '+': '-',
    '-': '+'
}


def solve(seq, width):
    count = 0
    j = 0
    while j + width <= len(seq):
        while seq[j] == '+':
            j += 1
            if j >= len(seq):
                return count
        if j + width > len(seq):
            return 'IMPOSSIBLE'
        for k in range(width):
            seq[j + k] = CAKES[seq[j + k]]
        count += 1
    return 'IMPOSSIBLE'

with open('2017_a.in') as f:
    with open('2017_a.out', 'w') as fo:
        lines = f.readlines()
        t = int(lines[0].strip())
        for i in range(1, t + 1):
            s, w = lines[i].strip().split()
            w = int(w)
            if not '-' in s:
                # print 'Case #{}: {}\n'.format(i, solve(s, w))
                fo.write('Case #{}: 0\n'.format(i))
                continue
            if w > len(s):
                # print 'Case #{}: {}\n'.format(i, solve(s, w))
                fo.write('Case #{}: IMPOSSIBLE\n'.format(i))
                continue
            s = list(s)
            # print 'Case #{}: {}\n'.format(i, solve(s, w))
            fo.write('Case #{}: {}\n'.format(i, solve(s, w)))
