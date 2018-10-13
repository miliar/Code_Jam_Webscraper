import sys
import re #regular expressions, string pattern matching
import math #math stuff
import array #more efficient lists (type constraint)

def solve(R,capacity,numgrps,groups):
    profit = 0
    grpptr = 0 #points to next grp in line
    for i in range(0,R):
        load = 0
        grpstaken = 0
        while ((load+groups[grpptr]) <= capacity):
            load = load + groups[grpptr]
            grpptr = grpptr + 1
            grpstaken = grpstaken + 1
            if (grpptr == numgrps):
                grpptr = 0
            if (grpstaken == numgrps):
                break
        profit = profit + load
    return profit

if __name__ == "__main__":
    cases = int(sys.stdin.readline().strip())
    for case in range(1,cases+1):
        print "Case #{0}:".format(case),
        #read and format input here
        input = map(int,sys.stdin.readline().strip().split())
        R = input[0]
        k = input[1]
        numgrps = input[2]
        groups = map(int,sys.stdin.readline().strip().split())

        #print solution
        print solve(R,k,numgrps,groups);