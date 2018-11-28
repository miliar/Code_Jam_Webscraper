
#!/usr/bin/python

import sys
import os
from collections import defaultdict, Counter

results = dict()


def mushrooms(input_filename):
    input_file = open(input_filename, "r")
    num_test_cases = int(input_file.readline().strip())
    for i in xrange(num_test_cases):
        N = int(input_file.readline().strip())
        all_mis = map(int, input_file.readline().strip().split())
        y = 0
        z = 0

        diff_list = [max(0, all_mis[j] - all_mis[j+1]) for j in xrange(N-1)]

        #method 1
        y = sum(diff_list)
        ##for j in xrange(N-1):
        ##    y += 

        #method 1
        max_rate = max(diff_list)
        for j in xrange(N-1):
            z += min(max_rate, all_mis[j])

        results[i+1] = (y, z)
    input_file.close()




def write_output():
    output_file = open("output.txt", "w")
    for k,v in results.iteritems():
        output_file.write("Case #"+str(k)+": "+str(v[0])+" "+str(v[1])+"\n")
    output_file.close()


if __name__ == "__main__":
    input_filename = sys.argv[1]
    mushrooms(input_filename)
    write_output()

#
