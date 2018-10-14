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

def solve(people):
    standing = 0
    retval = 0
    for idx, level in enumerate(people):
        if idx<=standing:
            standing += level
        elif level>0:
            retval += idx - standing
            standing += idx - standing + level
        print idx, level, standing
    
    return retval
    
def main():
    f = open(infile, "r")
    no_cases = read_int(f)

    for case_idx in xrange(no_cases):
        line = f.readline().rstrip()
        no_people, people = line.split(" ")
        no_people = int(no_people)
        people = map(int, people)
        result = solve(people)        
        out.write("Case #%d: %s\n" % (case_idx+1, result))
        
    out.close()
    
if __name__ == "__main__":
    main()
    
    