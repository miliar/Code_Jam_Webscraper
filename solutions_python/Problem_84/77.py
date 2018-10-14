#! /usr/bin/env python

import operator as op

A = {".":0, "0":0, "1":1}
B = {".":0, "0":1, "1":1}

for t in xrange(1, 1 + int(raw_input())):
    R, C = [int(x) for x in raw_input().split()]
    matrix = []
    for r in xrange(R):
        matrix.append(list(raw_input()))
    impossible = 0
    for r in xrange(R):
        for c in xrange(C):
            if matrix[r][c] == r"#":
                if r + 1 < R and c + 1 < C and \
                   matrix[r + 0][c + 1] == r"#" and \
                   matrix[r + 1][c + 0] == r"#" and \
                   matrix[r + 1][c + 1] == r"#":
                    matrix[r + 0][c + 0] = r"/"
                    matrix[r + 0][c + 1] = r"@"
                    matrix[r + 1][c + 0] = r"@"
                    matrix[r + 1][c + 1] = r"/"
                else:
                    impossible = 1
    print "Case #%d:" % t
    if impossible:
        print "Impossible"
    else:
        for r in xrange(R):
            print "".join(matrix[r]).replace("@", "\\")

# [EOF]
