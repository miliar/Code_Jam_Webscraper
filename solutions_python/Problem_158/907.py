#!/usr/bin/pypy

import sys
infile = sys.argv[1]
try:
    out = open(sys.argv[2], "w")
except IndexError:
    out = sys.stdout

def read_int(f):
    return int(f.readline())

def read_ints(f, sep=" "):
    return map(int, f.readline().rstrip().split(sep))

def read_lines(f, no_lines):
    retval = []
    for i in xrange(no_lines):
        retval.append(f.readline().rstrip())
    return retval


NO_WIN = "RICHARD"
WIN = "GABRIEL"

def solve(blocks, rows, cols):
    area = rows*cols
    if area % blocks != 0:
        return NO_WIN
    
    if (rows == 1 and cols == 1) and blocks > 1:
        return NO_WIN
        
    if (rows == 1 or cols == 1) and blocks > 2:
        return NO_WIN

    if (rows <= 2 or cols <= 2) and blocks > 3:
        return NO_WIN
    
    if (rows == 2 and cols == 2):
        if blocks == 1:
            return WIN
        if blocks == 2:
            return WIN
        if blocks >= 3:
            return NO_WIN
    
    return WIN
    
def main():
    f = open(infile, "r")
    no_cases = read_int(f)

#    for rows in xrange(1,5):
#        for cols in xrange(1,5):
#            for blocks in xrange(1,5):
#                print blocks, rows, cols, solve(blocks, rows, cols)

    for case_idx in xrange(no_cases):
        blocks, rows, cols = read_ints(f)
        result = solve(blocks, rows, cols)
        out.write("Case #%d: %s\n" % (case_idx+1, result))
        
    out.close()
    
if __name__ == "__main__":
    main()
