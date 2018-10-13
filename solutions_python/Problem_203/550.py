#!/usr/bin/env python3
import sys
import numpy as np

DATA = u'''3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
'''

def alphabet(x, oh=sys.stdout):
    m, n = x.shape
    d = 1
    while d > 0:
        c = np.sum(x == '?')
        left = x[:-1]
        right = x[1:]
        left[left == '?'] = right[left == '?']
        right[right == '?'] = left[right == '?']
        d = c - np.sum(x == '?')
    if c > 0:
        d = 1
    while d > 0:
        c = np.sum(x == '?')
        left = x[:, :-1]
        right = x[:, 1:]
        left[left == '?'] = right[left == '?']
        right[right == '?'] = left[right == '?']
        d = c - np.sum(x == '?')
    for row in x:
        oh.write(''.join(row) + '\n')

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        from io import StringIO
        fh = StringIO(DATA)
        oh = sys.stdout
    else:
        fh = open(sys.argv[1], 'r')
        oh = open('output.txt', 'w')
    with fh:
        with oh:
            case_num = 0
            for i, line in enumerate(fh.readlines()):
                if i == 0:
                    n = int(line)
                    c = 0
                    data = None
                elif c == 0:
                    m, n = [int(_) for _ in line.strip().split()]
                    c = m
                    if data is not None:
                        case_num += 1
                        oh.write('Case #{}:\n'.format(case_num))
                        alphabet(data, oh)
                    data = np.zeros((m, n), dtype=np.character)
                else:
                    data[m - c] = list(line.strip())
                    c -= 1
            case_num += 1
            oh.write('Case #{}:\n'.format(case_num))
            alphabet(data, oh)

