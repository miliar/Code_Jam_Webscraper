#!/usr/bin/python

import sys

n_size = 100000

def solve(C, F, X, outf):
    if (C >= X):
        outf.write(str(X/2))
        return

    xint = 0
    ptime = 1000000000
    for n in range(n_size):
        time = X/(2+n*F) + xint
        if (time > ptime):
            outf.write("{0:.7f}".format(ptime))
            return
        xint += C/(2.0+n*F)
        ptime = time

def solve_all(C, F, X, outf):
    if (C >= X):
        outf.write(str(X))
        return

    xint = 0
    ptime = 1000000000
    for n in range(n_size):
        time = X/(2+n*F) + xint
        print("n = {0}, time = {1}".format(n, time))
        xint += C/(2.0+n*F)
        ptime = time

def run():
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    inf = open(infilename, 'r')
    outf = open(outfilename, 'w')

    cases_num = int(inf.readline())

    for i in range(cases_num):
        outf.write("Case #{0}: ".format(i+1))
        data = (inf.readline()).split()
        
        solve(float(data[0]), float(data[1]), float(data[2]), outf)
        
        outf.write("\n")

    inf.close()
    outf.close()

if __name__ == "__main__":
    run()
    #outf = open("p2.out", 'w')
    #solve(306.0000, 2.00000, 612, outf)

