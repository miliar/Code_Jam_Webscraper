#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import sys
def read_line(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline())
INF = float('inf')

def solve():
    # Read a problem
    N = read_int()
    lines = []
    for i in range(N):
        lines.append(read_line())

    result = 0
    while len(lines[0]) > 0:
        ch = lines[0][0]
        counts = [0] * N
        for i in range(len(lines)):
            while len(lines[i]) > 0 and lines[i][0] == ch:
                counts[i] += 1
                lines[i] = lines[i][1:]
            if counts[i] == 0:
                return 'Fegla Won'
        mean = int(round(sum(counts) / N))
        result += sum([int(abs(x - mean)) for x in counts])
    for s in lines:
        if len(s) > 0:
            return 'Fegla Won'

    return result

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: {}'.format(i+1, solve()))
