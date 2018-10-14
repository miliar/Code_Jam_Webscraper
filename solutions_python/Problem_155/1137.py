#!/usr/bin/env python
import sys

# initialization
input_file = open(sys.argv[1])
line_count = 0
max_lines = 0
debug_flag = True

# number of test cases
line = input_file.readline().strip()
T = int(line)

# determine outcome 
def result(s_str):
    S = [int(v) for v in s_str]
    standing = 0
    extras = 0
    for i,s in enumerate(S):
        if standing < i:
            extras += (i - standing)
            standing += (i - standing)
        standing += s 
    return extras

# main method
def main():
    # process each case
    for t in xrange(0,T):

        s_max,s_str = input_file.readline().strip().split()
        print "Case #%d: %s" % (t+1,result(s_str))
        
if __name__ == '__main__':
    main()
