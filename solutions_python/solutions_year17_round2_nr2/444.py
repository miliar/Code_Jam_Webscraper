import math
from collections import defaultdict
import operator


def find(cur, m, first):
    if first and cur != first:
        if m[first]:
            return first
    sorted_m = sorted(m.items(), key=lambda x: x[1], reverse=True)
    for v in sorted_m:
        if cur == v[0]:
            continue
        if v[1] <= 0:
            continue
        return v[0]
    return -1


def solve(test, input, output):
    print('Solving #{}'.format(test))

    line = input.readline()
    N = int(line.split()[0])
    m = {}
    m['R'] = int(line.split()[1])
    m['Y'] = int(line.split()[3])
    m['B'] = int(line.split()[5])


    o = ''
    for k, v in m.items():
        if v > N / 2:
            o = 'IMPOSSIBLE'
            break
    if o != 'IMPOSSIBLE':
        for i in range(N):
            if i == 0:
                c = find('', m, None)
                if c == -1:
                    o = 'IMPOSSIBLE'
                    break
                o += c
                m[c] -= 1
            else:
                c = find(o[i - 1], m, o[0])
                if c == -1:
                    o = 'IMPOSSIBLE'
                    break
                o += c
                m[c] -= 1


    out = 'Case #{0}: {1}'.format(test, o)
    print(out)
    output.write(out + '\n')


with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
    test_cases = int(input.readline())
    for test in range(1, test_cases + 1):
        solve(test, input, output)
