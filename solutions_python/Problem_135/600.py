#!/usr/bin/env python

import sys, os, re

#---------------------------------------------------
# Variable 
#---------------------------------------------------

#---------------------------------------------------
# Function 
#---------------------------------------------------
def check_trick(sel1, grid1, sel2, grid2):
    row1 = set(grid1[sel1-1])
    row2 = set(grid2[sel2-1])
    final = list(row1 & row2)
    return final

def load_file(filename):
    dict = {'X':'X won', 'O': 'O won', None:'Game has not completed', 'D':'Draw'}
    with open(filename, 'rU') as f:
        number = int(f.readline())
        for n in range(number):
            sel1 = int(f.readline())
            grid1 = []
            for i in range(4):
                grid1.append([ int(s) for s in f.readline().strip().split(' ')])

            sel2 = int(f.readline())
            grid2 = []
            for i in range(4):
                grid2.append([ int(s) for s in f.readline().strip().split(' ')])

            result = check_trick(sel1, grid1, sel2, grid2)

            print "Case #%d:" % (n+1),
            if len(result) == 1:
                print result[0] 
            elif len(result) == 0:
                print "Volunteer cheated!"
            else:
                print "Bad magician!"
    return

#---------------------------------------------------
# Entry Point 
#---------------------------------------------------
def main():
    load_file (sys.argv[1])

    return

#---------------------------------------------------
# Unit Test Entry 
#---------------------------------------------------
if __name__ == '__main__':
    main()


