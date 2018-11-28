#!/usr/bin/python

import sys
import os
from collections import defaultdict, Counter

results = dict()


def mushrooms(input_filename):
    input_file = open(input_filename, "r")
    num_test_cases = int(input_file.readline().strip())
    for i in xrange(num_test_cases):
        R,C,W = map(int, input_file.readline().strip().split())
        if W == 1:
            answer = R*C
        elif W == C:
            num_until_hit = R
            remaining_hits = W-1
            answer = num_until_hit+remaining_hits
        else:
            num_per_row = C/W
            num_until_hit = R*num_per_row
            misses_after_hit = 0 if C%W == 0 else 1
            remaining_hits = W-1
            answer = num_until_hit+misses_after_hit+remaining_hits
        results[i+1] = answer
    input_file.close()



def write_output():
    output_file = open("output.txt", "w")
    for k,v in results.iteritems():
        output_file.write("Case #"+str(k)+": "+str(v)+"\n")
    output_file.close()


if __name__ == "__main__":
    input_filename = sys.argv[1]
    mushrooms(input_filename)
    write_output()

#
