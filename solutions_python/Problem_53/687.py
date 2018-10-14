import sys
import re #regular expressions, string pattern matching
import math #math stuff
import array #more efficient lists (type constraint)

def solve(input):
    devices = 2**input[0]
    snaps = input[1]
    x = snaps % (devices)
    if ((devices - x) == 1):
        return "ON"
    return "OFF"

if __name__ == "__main__":
    cases = int(sys.stdin.readline().strip())
    for case in range(1,cases+1):
        print "Case #{0}:".format(case),
        #read and format input here
        input = map(int,sys.stdin.readline().strip().split())

        #print solution
        print solve(input);