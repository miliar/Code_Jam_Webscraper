#!/usr/bin/env python
import sys

def read_line(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]

def val(ch):
    if ch == 'X': return 1
    if ch == 'O': return 10
    if ch == 'T': return 100
    else: return -1000  # empty

def solve(lines):
    sums = []
    # horizontal
    sums.append(val(lines[0][0]) + val(lines[0][1]) + val(lines[0][2]) + val(lines[0][3]))
    sums.append(val(lines[1][0]) + val(lines[1][1]) + val(lines[1][2]) + val(lines[1][3]))
    sums.append(val(lines[2][0]) + val(lines[2][1]) + val(lines[2][2]) + val(lines[2][3]))
    sums.append(val(lines[3][0]) + val(lines[3][1]) + val(lines[3][2]) + val(lines[3][3]))
    # vertical
    sums.append(val(lines[0][0]) + val(lines[1][0]) + val(lines[2][0]) + val(lines[3][0]))
    sums.append(val(lines[0][1]) + val(lines[1][1]) + val(lines[2][1]) + val(lines[3][1]))
    sums.append(val(lines[0][2]) + val(lines[1][2]) + val(lines[2][2]) + val(lines[3][2]))
    sums.append(val(lines[0][3]) + val(lines[1][3]) + val(lines[2][3]) + val(lines[3][3]))
    # diagonal
    sums.append(val(lines[0][0]) + val(lines[1][1]) + val(lines[2][2]) + val(lines[3][3]))
    sums.append(val(lines[0][3]) + val(lines[1][2]) + val(lines[2][1]) + val(lines[3][0]))

    can_continue = False
    for v in sums:
        if v < 0:
            can_continue = True
            continue
        if v == 4 or v == 103:
            return 'X won'
        if v == 40 or v == 130:
            return 'O won'

    if can_continue:
        return 'Game has not completed'
    else:
        return 'Draw'

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        lines = []
        for j in range(4):
            lines.append(read_line())
        print('Case #{}: {}'.format(i+1, solve(lines)))
        read_line()

