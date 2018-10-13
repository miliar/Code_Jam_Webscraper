#! /usr/bin/env python
import sys

sample = "sample"

if len(sys.argv) < 2:
    print "usage: %s [sample | name]" % (sys.argv[0], )
    sys.exit(1)

if sys.argv[1].lower() == "sample":
    fin = open(sample + ".in", "r") 
    fout = open(sample + ".out", "w")
else:
    fin = open(sys.argv[1], "r")
    fout = open(sys.argv[1] + ".out", "w")

matrix = []
case = 1
ncases = int(fin.readline())

def get_col(mat, coln):
    return tuple([r[coln] for r in mat])

def get_row(mat, row):
    return tuple(mat[row])

def can_cut(matrix):
    mat = matrix
    while len(mat) > 0 and len(mat[0]) > 0:
        flat = [n for row in mat for n in row]
        minimum = min(flat)
        for r in xrange(0, len(mat)):
            row = get_row(mat, r)
            ucan = all(n == minimum for n in row)
            if ucan == True:
                mat.pop(r)
                break
        if ucan == True: continue
        for c in xrange(0, len(mat[0])):
            col = get_col(mat, c)
            ucan = all(n == minimum for n in col)
            if ucan == True:
                for row in mat:
                    row.pop(c)
                break
        else:
            # the loop should end by continues
            # this happens if the min is not the only number in row / col 
            return False
        continue

    return True

while True:
    line = fin.readline()
    line = line.rstrip()

    parts = line.split()
    N = int(parts[0])
    M = int(parts[1])

    for n_ in xrange(0, N):
        line = fin.readline()
        line = line.strip()
        numbers = line.split()
        matrix.append([int(num) for num in numbers])
    
    if can_cut(matrix):
        msg = "Case #%d: %s\n" % (case, "YES")
    else:
        msg = "Case #%d: %s\n" % (case, "NO")

    print msg,
    fout.write(msg)
    matrix = []
    case += 1

    if case > ncases:
        break

fin.close()
fout.close()
