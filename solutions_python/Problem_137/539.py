#!/usr/bin/env python

def draw_board(R, C, safe_list):
    strings = []

    # safe_list is column count of safe cells by row
    for row in range(R):
        if len(safe_list) > row:
            if row == 0:
                if (safe_list[row]) == 0:
                    strings.append('c' + '*' * (C - safe_list[row] - 1))
                else:
                    strings.append('c' + '.' * (safe_list[row] - 1) + '*' * (C - safe_list[row]))
            else:
                strings.append('.' * safe_list[row] + '*' * (C - safe_list[row]))
        else:
            strings.append('*' * C)

    return '\n'.join(strings)


def breakout(bin_count, bin_size, item_count):
    if item_count < 0:
        return None
    elif item_count == 0:
        return []
    elif item_count == 1 or bin_count == 0:
        return None

    for d in range(2, bin_size + 1):
        bins = breakout(bin_count - 1, d, item_count - d)
        if bins is not None:
            return [d] + bins

    return None


def run_one(R, C, M):
    safe_cells = R * C - M

    if safe_cells == 1:
        return draw_board(R, C, [0] * R)

    if R == 1 and C == 1:
        return draw_board(R, C, [1])
    elif R == 1:
        return draw_board(R, C, [safe_cells])
    elif C == 1:
        return draw_board(R, C, [1] * safe_cells)
    else:
        for d in range(2, C + 1):
            # break number into X bins where no bin has < 2 and first bin = second bin
            bins = breakout(R - 2, d, safe_cells - 2 * d)
            if bins is not None:
                return draw_board(R, C, [d, d] + bins)

        return 'Impossible'


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        R, C, M = [int(x) for x in lines.popleft().split()]

        result = run_one(R, C, M)

        output.append('Case #{0}:'.format(t + 1))
        output.append(result)

    return output


# Google Code Jam submissions must run stand-alone.
# This code shall be copied into each solution.
if __name__ == '__main__':
    import os
    import sys
    from collections import deque

    infile = sys.argv[1]
    with open(infile) as file:
        lines = deque(file.readlines())
        output = run(lines)
        print os.linesep.join(output)
