#!/usr/bin/env python
import sys, itertools

X_or_T = lambda char: char in 'XT'
O_or_T = lambda char: char in 'OT'

def process(linebuffer):
    rows, cols, diags = ([], [], [], []), ([], [], [], []), ([], [])
    for i, line in enumerate(linebuffer):
        for j, char in enumerate(line):
            rows[i].append(char)
            cols[j].append(char)
            if i == j:
                diags[0].append(char)
            if i == 3-j:
                diags[1].append(char)

    if any(all(X_or_T(char) for char in line) for line in itertools.chain(rows, cols, diags)):
        return 'X won'

    if any(all(O_or_T(char) for char in line) for line in itertools.chain(rows, cols, diags)):
        return 'O won'

    if any('.' in line for line in itertools.chain(rows, cols, diags)):
        return 'Game has not completed'

    return 'Draw'

if __name__ == '__main__':
    # ignore first line (we read all input, no need to count it)
    sys.stdin.readline()

    numcase, lineno, linebuffer = 1, 0, []
    for line in sys.stdin:
        if lineno == 4:
            print "Case #%d: %s" % (numcase, process(linebuffer))
            lineno, linebuffer = 0, []
            numcase += 1
            continue

        linebuffer.append(line.strip())
        lineno += 1

