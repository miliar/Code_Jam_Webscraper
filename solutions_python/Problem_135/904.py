#!/usr/bin/env python

def guess_number(lines):
    first_choice = int(lines[0])
    first_numbers = lines[first_choice]
    second_choice = int(lines[5])
    second_numbers = lines[5+second_choice]

    first_numbers = set(first_numbers.split())
    second_numbers = set(second_numbers.split())
    numbers = first_numbers & second_numbers
    if len(numbers) == 0:
        return "Volunteer cheated!"
    elif len(numbers) == 1:
        return numbers.pop()
    else:
        return "Bad magician!"
    
import sys
#import pdb

if __name__ == '__main__':
    filename_prefix = sys.argv[1]
    filename_in = filename_prefix + ".in"
    filename_out = filename_prefix + ".out"

    file_in = open(filename_in, 'r')
    lines = file_in.readlines()
    testcnt = int(lines[0])
    idx = 1
    file_out = open(filename_out, 'w')
    
    #pdb.set_trace()
    for test in range(testcnt):
        res = guess_number(lines[idx : idx + 10])
        file_out.write("Case #{0}: {1}\n".format(test + 1, res))
        idx += 10
