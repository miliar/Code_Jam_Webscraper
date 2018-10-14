#!/usr/bin/env python
import sys


def solve(ans1, grid1, ans2, grid2):
    row1 = grid1[ans1 - 1]
    row2 = grid2[ans2 - 1]

    possible = [x for x in row1 if x in row2]
    if len(possible) == 1:
        return possible[0]
    elif len(possible) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


if __name__ == '__main__':
    # Read args
    if len(sys.argv) < 2:
        print "USAGE: a.py in_file.in out_file.out"

    with open(sys.argv[1], 'rU') as fin, open(sys.argv[2], 'w') as fout:
        T = int(fin.readline())

        for case in xrange(1, T+1):
            ans1 = int(fin.readline().strip())
            grid1 = [map(int, fin.readline().split()) for i in range(4)]

            ans2 = int(fin.readline().strip())
            grid2 = [map(int, fin.readline().split()) for i in range(4)]

            soln = solve(ans1, grid1, ans2, grid2)

            print >> fout, "Case #{0}: {1}".format(case, soln)
