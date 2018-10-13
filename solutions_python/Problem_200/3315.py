# -*- coding: utf-8 -*-


def solve(number):
    seq = [int(x) for x in list(number)]
    j = len(seq) - 1
    last_9 = len(seq)
    while j >= 1:
        if seq[j] < seq[j - 1]:
            last_9 = j
            seq[j - 1] -= 1
        j -= 1
    for j in range(last_9, len(seq)):
        seq[j] = 9
    return ''.join(str(x) for x in seq).lstrip('0')

with open('2017_b.in') as f:
    with open('2017_b.out', 'w') as fo:
        lines = f.readlines()
        t = int(lines[0].strip())
        for i in range(1, t + 1):
            n = lines[i].strip()
            # print 'Case #{}: {}\n'.format(i, solve(n))
            fo.write('Case #{}: {}\n'.format(i, solve(n)))
