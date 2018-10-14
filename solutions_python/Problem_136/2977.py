import numpy as np
import os
import re

def main():
    infile = "Blarge.in"
    inf = open(infile, 'r')

    outfile = "Blarge.out"
    outf = open(outfile, 'w')

    lnum = 0
    case = 0
    totcase = 0
    for line in inf:
        if (lnum == 0):
            totcase = int(line.split()[0])
        else:
            case += 1
            sp = line.split()
            c = float(sp[0])
            f = float(sp[1])
            x = float(sp[2])
            farmtime = 0.
            ncurr = x/2.
            nbest = ncurr
            n = 0
            while(ncurr == nbest):
                n += 1
                farmtime += c / (2. + (n-1.)*f)
                ncurr = x/(2.+n*f) + farmtime
                if (ncurr < nbest):
                    nbest = ncurr
            outf.write(("Case #" + str(case) + ": " + '%.7f' + "\n") % nbest)
            string1 = ''
            string2 = ''
            row1 = 0
            row2 = 0
            answer = 0
        lnum += 1
            


if __name__ == '__main__':
     main()
