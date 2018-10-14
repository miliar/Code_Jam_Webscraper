
#!/usr/bin/python

import sys
import os
from collections import defaultdict, Counter

results = dict()


def stand_oval(input_filename):
    input_file = open(input_filename, "r")
    num_test_cases = int(input_file.readline().strip())
    for i in xrange(num_test_cases):
        max_shy_str, shy_count_str = input_file.readline().strip().split()
        shy_count = [int(c) for c in shy_count_str]
        min_friends = 0
        total_standing = 0
        #print(max_shy_str, shy_count)
        for j in xrange(int(max_shy_str)):
            total_standing += shy_count[j]
            #print("   "+str((total_standing, j+1, min_friends)))
            if total_standing < j+1:
                min_friends += j+1 - total_standing
                total_standing = j+1
        results[i+1] = min_friends
    input_file.close()




def write_output():
    output_file = open("output.txt", "w")
    for k,v in results.iteritems():
        output_file.write("Case #"+str(k)+": "+str(v)+"\n")
    output_file.close()


if __name__ == "__main__":
    input_filename = sys.argv[1]
    stand_oval(input_filename)
    write_output()

#
