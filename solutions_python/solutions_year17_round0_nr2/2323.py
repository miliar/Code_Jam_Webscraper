#!usr/bin/env python

"""
Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.


Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.


Limits
1 ≤ T ≤ 100.
"""


import sys


def file_reader(input_file):
    with open(input_file, 'r') as file_obj_in:
         lines = file_obj_in.readlines()
         return lines

def find_last_tidy(last_number):
    if last_number < 10:
        return last_number
    num_str = str(last_number)
    digits = len(num_str)
    prev = int(num_str[0])
    for i in range(1, digits):
        current = int(num_str[i])
        j = i
        while prev > current:
            prev -= 1
            places = digits - j
            j -= 1
            num_str = num_str[:j] + str(prev) + places*'9'
            current = prev
            if j > 0:
                prev = int(num_str[j-1]) 
        prev = int(num_str[i])
    return num_str.lstrip('0')

def main(filename, output):
    lines = file_reader(filename)
    testcases = int(lines[0].strip())
    i = 0
    output_file = output
     
    while i < testcases:
        i += 1
        last_number = int(lines[i].strip())
        last_tidy_number = find_last_tidy(last_number)            

        with open(output_file, 'a') as file_obj_out:
            file_obj_out.write("Case #" + str(i) + ": " + str(last_tidy_number) + "\n")


if __name__ == '__main__':
    filename = sys.argv[1]
    output = sys.argv[2]
    main(filename, output)
