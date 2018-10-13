"""
Codejam 2015 - Round1A
"""
import sys

def problem_a(row, column, width):
    coup = 0
    print >> sys.stderr, "%s %s %s" % (row, column, width)

    if width == 1:
        return row * column
    if width == column:
        return row - 1 + column

    restant = column

    while restant > 0:

        if width == restant:
            coup += width
            break

        if 2*width > restant:
            coup += width + 1
            break

        coup += 1
        restant -= width

    return coup * row

T = int(raw_input())
CASES = []
for i in xrange(T):
    row, column, width = [int(j) for j in raw_input().split()]
    print "Case #%s: %s" % (i+1, problem_a(row, column, width))


