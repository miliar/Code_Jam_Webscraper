from __future__ import print_function

import fractions
import sys

def calc(cake):
    rows = [list(s) for s in cake]
    R = len(rows)
    C = len(rows[0])

    first_pos_by_row = [None] * R
    first_good_row = None

    # Fill in rows to the right.
    for i, row in enumerate(rows):
        first_char_pos = None
        last_char = None
        for j in range(C):
            ch = row[j]
            if ch == '?':
                if last_char is not None:
                    row[j] = last_char
            else:
                if first_char_pos is None:
                    first_char_pos = j
                last_char = ch
        first_pos_by_row[i] = first_char_pos
        if first_char_pos is not None:
            if first_good_row is None:
                first_good_row = i

    assert first_good_row is not None

    # Fill in rows to the left.
    for i, row in enumerate(rows):
        first_pos = first_pos_by_row[i]
        if first_pos is None:
            continue
        for j in range(first_pos):
            row[j] = row[first_pos]

    # Extent good rows down.
    last_good_row = None
    for i in range(R):
        first_pos = first_pos_by_row[i]
        if first_pos is None:
            if last_good_row is not None:
                rows[i] = list(rows[last_good_row])
        else:
            last_good_row = i

    assert last_good_row is not None

    # Extend the first good row up.
    for i in range(first_good_row):
        rows[i] = list(rows[first_good_row])

    filled_cake = [''.join(x) for x in rows]
    return filled_cake

def main():
    f = sys.stdin

    if len(sys.argv) > 1:
        f = open(sys.argv[1], "rt")

    T = int(f.readline().strip())

    for case_id in range(1, T+1):
        R, C = map(int, f.readline().strip().split())
        cake = []
        for i in range(R):
            row = f.readline().strip()
            assert len(row) == C, '{} {}'.format(len(row), C)
            cake.append(row)

        r = calc(cake)

        print('Case #{}:'.format(case_id))
        for row in r:
            print(row)

if __name__ == '__main__':
    main()
    # do_stuff()
