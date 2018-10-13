#/usr/bin/python
# Author: Cagil Ulusahin
# Date: 12 April 2014

import sys
from sets import Set

def main(argv):
    if(len(argv) > 0):
        infile = argv[0]
    readFile(infile)


def readFile(infile):
    with open(infile) as f:
        T = int(f.readline())
        for t in range(0,T):
            row1 = get_row(f)
            row2 = get_row(f)
            answer = row1 & row2
            #print answer
            #print row1,row2
            if len(answer) == 0:
                print("Case #%d: Volunteer cheated!" %(t+1))
            elif len(answer) == 1:
                print("Case #%d: %s" %((t+1),answer.pop()))
            else:
                print("Case #%d: Bad magician!" %(t+1))
def get_row(f):
    answer1 = int(f.readline())
    read_n_line(f,answer1-1)
    line = f.readline().strip("\n").split(" ")
    row1 = Set(line)
    read_n_line(f,4-answer1)
    return row1

def read_n_line(f,n):
    for a in range(0,n):
        f.readline()

if __name__ == "__main__":
    main(sys.argv[1:])
