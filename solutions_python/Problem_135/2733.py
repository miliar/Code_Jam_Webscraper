# -*- coding: utf-8 -*-
import sys
from numpy import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python {0} inputfile".format(sys.argv[0])
        quit()

    ifile = open(sys.argv[1])
    ofile = open("output.txt", 'w')
    N = ifile.readline()

    for case in range(int(N)):
        arrange = [[0 for j in range(4)] for i in range(2)]
        for t in range(2):
            ans_row = ifile.readline()
            for row in range(4):
                tmp = ifile.readline()
                if row == int(ans_row) -1:
                    arrange[t] = tmp.rstrip().split()

        ret = "Volunteer cheated!"
        count = 0
        for c1 in arrange[0]:
            if c1 in arrange[1]:
                count = count + 1
                tmp = c1

        if count > 1:
            ret = "Bad magician!"
        elif count == 1:
            ret = tmp

        print "Case #{0}: {1}".format(case + 1, ret)
        ofile.write("Case #{0}: {1}\n".format(case + 1, ret))

    ifile.close()
    ofile.close()

