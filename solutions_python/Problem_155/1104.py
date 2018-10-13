#!/usr/bin/env python

import sys

def solve(input_line):
    max_shyness = int(input_line.split()[0])
    people = [int(d) for d in input_line.split()[1]]

    friends_needed = 0
    standing = 0

    for shyness_level, count in enumerate(people):
        if standing < shyness_level:
            delta = shyness_level - standing
            friends_needed += delta
            standing += delta
            standing += count
        else:
            standing += count

    return friends_needed

    
if __name__ == '__main__':
    input_file_name = sys.argv[1]
    input_file = open(input_file_name)
    number_of_cases = int(input_file.readline().strip())

    first_case_number = 1
    for x in xrange(number_of_cases):
        input_line = input_file.readline().strip()
        print "Case #{case_number}: {friend_count}".format(
            case_number=(first_case_number + x),
            friend_count=solve(input_line)
        )
