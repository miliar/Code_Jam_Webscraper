#!/usr/bin/python

import sys
import os
from collections import defaultdict, Counter

results = dict()

def mean(lst):
    return sum(lst)*1.0/len(lst)

def count_overlap(string, substr):
    count = start_idx = 0
    while True:
        start_idx = string.find(substr, start_idx) + 1
        if start_idx > 0:
            count += 1
        else:
            return count

def mushrooms(input_filename):
    input_file = open(input_filename, "r")
    num_test_cases = int(input_file.readline().strip())
    for i in xrange(num_test_cases):
        K,L,S = map(int, input_file.readline().strip().split())
        Kstr = input_file.readline().strip()
        Lstr = input_file.readline().strip()

        if not set(Kstr).issuperset(set(Lstr)):
            answer = 0.0
        elif len(set(Kstr)) == 1:
            answer = 0.0
        else:
            all_possible_str = [""]
            for idx in xrange(S):
		print(idx, len(all_possible_str))
		sys.stdout.flush()
                new_possible_str = []
                for x in all_possible_str:
                    new_possible_str += [c+x for c in Kstr]
                all_possible_str = new_possible_str
            all_counts = [count_overlap(x, Lstr) for x in all_possible_str]
            answer = max(all_counts) - mean(all_counts)
        print(answer)
        sys.stdout.flush()
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
