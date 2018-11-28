
#!/usr/bin/python

import sys
import os
from collections import defaultdict, Counter

results = dict()

DEBUG=False

def nominos(input_filename):
    input_file = open(input_filename, "r")
    num_test_cases = int(input_file.readline().strip())
    for i in xrange(num_test_cases):
        X, R, C = map(int, input_file.readline().strip().split())
        possible_win = False
        if R*C % X != 0:
            possible_win = False
        elif X == 1:
            possible_win = True
        elif X == 2:
            possible_win = True
        elif X == 3:
            if R != 1 and C != 1:
                possible_win = True
        elif X == 4:
            if R*C / X <= 2:
                possible_win = False
            else:
                possible_win = True
        else:
            raise Exception("Solution incomplete")

        results[i+1] = "GABRIEL" if possible_win else "RICHARD"
    input_file.close()




def write_output():
    output_file = open("output.txt", "w")
    for k,v in results.iteritems():
        output_file.write("Case #"+str(k)+": "+str(v)+"\n")
    output_file.close()


if __name__ == "__main__":
    input_filename = sys.argv[1]
    nominos(input_filename)
    write_output()

#
