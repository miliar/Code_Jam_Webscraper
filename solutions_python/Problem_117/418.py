#!/usr/bin/env python
# Lawn mow
# Author:  Yotam Medini  yotam.medini@gmail.com -- Created: 2013/April/13
import sys

fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

def get_io(argv):
    fin = sys.stdin
    fout = sys.stdout
    ifn = ofn = "-"
    if len(argv) == 2:
        bfn = sys.argv[1]
        ifn = bfn + '.in'
        ofn = bfn + '.out'
    if len(argv) > 2:
        ifn = argv[1]
        ofn = argv[2]
    if ifn != '-':
        fin = open(ifn, "r")
    if ofn != '-':
        fout = open(ofn, "w")
    return (fin, fout)

def get_numbers():
    line = fin.readline()
    return map(int, line.split())

def get_number():
    return get_numbers()[0]

def get_line():
    line = fin.readline()
    if len(line) > 0 and line[-1] == '\n':
        line = line[:-1]
    return line

def get_string():
    line = fin.readline()
    return line.strip()


class LawnMower:

    def __init__(self, nr, nc):
        self.nr = nr # #rows
        self.nc = nc # #columns
        self.a = []

    def row_add(self, row):
        self.a.append(row)

    def judge(self):
        # Compute max
        rows_max = self.nr * [0]
        cols_max = self.nc * [0]
        for i in range(self.nr):
            for j in range(self.nc):
                v = self.a[i][j]
                if rows_max[i] < v:
                    rows_max[i] = v
                if cols_max[j] < v:
                    cols_max[j] = v

        # Now ensure all each square
        # is not less than both max of its row&col
        ok = True
        i = 0
        while ok and i < self.nr:
            j = 0
            while ok and j < self.nc:
                # self.log("i=%d, j=%d" % (i, j))
                v = self.a[i][j]
                if v < rows_max[i] and v < cols_max[j]:
                    self.log0("Failed for (i=%d,j=%d) v=%d" %
                             (i, j, v))
                    ok = False
                j += 1
            i += 1
        self.result = "YES" if ok else "NO"


    def log(self, msg):
        sys.stderr.write("%s\n" % msg)

    def log0(self, msg):
        pass


if __name__ == "__main__":
    (fin, fout) = get_io(sys.argv)
    n_cases = get_number()
    for ci in range(n_cases):
        [nr, nc] = get_numbers()
        # sys.stderr.write("ci=%d, nr=%d, nc=%d\n" % (ci, nr, nc))
        lm = LawnMower(nr, nc)
        for i in range(nr):
            lm.row_add(get_numbers())
        lm.judge()
        fout.write("Case #%d: %s\n" % (ci + 1, lm.result))

    fin.close()
    fout.close()
    sys.exit(0)

                   
