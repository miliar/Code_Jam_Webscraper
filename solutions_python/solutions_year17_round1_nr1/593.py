#!/usr/bin/python
"""
Alphabet Cake
"""
import sys, os


def fill_row(row):
    is_to_fill = []
    filler = ""
    for i, l in enumerate(row):
        if l == "?":
            if filler:
                row[i] = filler
            else:
                is_to_fill.append(i)
        else:
            filler = l
            if is_to_fill:
                for e_i in is_to_fill:
                    row[e_i] = filler
                is_to_fill = []
    return row


def solve(w, h, grid):
    """Returns a string result to one case of a problem"""
    ys_to_fill = []
    filler = ""
    for y, row in enumerate(grid):
        grid[y] = fill_row(row)
        if row[0] == "?":
            if filler:
                grid[y] = filler
            else:
                ys_to_fill.append(y)
        else:
            filler = row
            if ys_to_fill:
                for e_y in ys_to_fill:
                    grid[e_y] = filler
                ys_to_fill = []
    result = ""
    for line in grid:
        result += "".join(line) + "\n"
    return "\n{}".format(result)[:-1]


# Shared########################################################################
def main():
    with open(sys.argv[1], 'rU') as f_in:
        cases = int(f_in.readline().strip())
        for case in range(1, cases + 1):
            # Get input data
            grid = []
            r, c = [int(x) for x in f_in.readline().strip().split()]
            for e_r in range(r):
                strip_ = [ch for ch in f_in.readline().strip()]
                grid.append(strip_)
            # Solve and output
            print("Case #{}: {}".format(case, solve(c, r, grid)))


if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        main()
    elif len(sys.argv) > 1 and not os.path.exists(sys.argv[1]):
        print "File '" + str(sys.argv[1]) + "' does not exist!"
    else:
        print "No file supplied! Run program this way: '" + str(
            sys.argv[0]) + " something.in'"
