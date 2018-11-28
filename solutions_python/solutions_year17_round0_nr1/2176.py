#!usr/bin/env python

"""
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S and an integer K. S represents the row of pancakes: each of its characters is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up).


Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is either IMPOSSIBLE if there is no way to get all the pancakes happy side up, or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it.


Limits

1 ≤ T ≤ 100.
Every character in S is either + or -.
2 ≤ K ≤ length of S.
"""


import sys


def file_reader(input_file):
    with open(input_file, 'r') as file_obj_in:
         lines = file_obj_in.readlines()
         return lines

def flip(flipper_range):
    flipped = ''
    for pancake in flipper_range:
        if pancake == '-':
            flipped += '+'
        else:
            flipped += '-'
    return flipped 
          
def calc_optimal_flips(row_of_pancakes, flipper_size):
    row_width = len(row_of_pancakes)
    happy_side = '+'
    blank_side = '-'
    optimal_flips = 0
    failure = 'IMPOSSIBLE'

    if blank_side not in row_of_pancakes:
        return optimal_flips
    elif flipper_size > row_width:
        return failure
    else:
        start = row_width - flipper_size + 1
        end = row_width
        while start > 0:
            start -= 1
            end -= 1
            while end >= 0 and row_of_pancakes[end] == '+':
                start -= 1
                end -= 1
            if start > -1 and blank_side in row_of_pancakes[start: end+1]:
                optimal_flips += 1
                flipped = flip(row_of_pancakes[start: end+1])
                row_of_pancakes = row_of_pancakes[:start] + flipped + row_of_pancakes[end+1:]
    if blank_side in row_of_pancakes:
        return failure
    else:
        return optimal_flips


def main(filename, output):
    lines = file_reader(filename)
    testcases = int(lines[0].strip())
    i = 0
    output_file = output

     
    while i < testcases:
        i += 1
        row_of_pancakes, flipper_size = lines[i].strip().split()
        flipper_size = int(flipper_size)

        with open(output_file, 'a') as file_obj_out:
            result = calc_optimal_flips(row_of_pancakes, flipper_size)
            file_obj_out.write("Case #" + str(i) + ": " + str(result) + "\n")


if __name__ == '__main__':
    filename = sys.argv[1]
    output = sys.argv[2]
    main(filename, output)
