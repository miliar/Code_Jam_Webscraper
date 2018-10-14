#!/usr/bin/env python3

"""
Input

The first line of the input gives the number of test cases, T; T test cases follow. Each test case begins with two integers D and N: the destination position of all of the horses (in kilometers) and the number of other horses on the road. Then, N lines follow. The i-th of those lines has two integers Ki and Si: the initial position (in kilometers) and maximum speed (in kilometers per hour) of the i-th of the other horses on the road.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum constant speed (in kilometers per hour) that Annie can use without colliding with other horses. y will be considered correct if it is within an absolute or relative error of 10-6 of the correct answer. See the FAQ for an explanation of what that means, and what formats of real numbers we accept.

Limits

1 ≤ T ≤ 100.
0 < Ki < D ≤ 109, for all i.
Ki ≠ Mj, for all i ≠ j. (No two horses start in the same position.)
1 ≤ Si ≤ 10000.
"""


import sys


def file_reader(input_file):
    with open(input_file, 'r') as file_obj_in:
         lines = file_obj_in.readlines()
         return lines

def unimpeded_time(start_pos, end_pos, speed):
    return (end_pos - start_pos)/speed

def main(file_in, file_out):
    lines = file_reader(file_in)

    tests = int(lines[0].strip())
    i = 0
    case = 0 

    while case < tests:
        case += 1
        i += 1

        end_pos, horses = lines[i].strip().split()
        end_pos, horses = int(end_pos), int(horses)

        slowest_time = 0
        for h in range(horses):
            i += 1
            start_pos, speed = lines[i].strip().split()
            start_pos, speed = int(start_pos), int(speed)
            time = unimpeded_time(start_pos, end_pos, speed)
            slowest_time = max(time, slowest_time)
        
        cruise_speed = end_pos/slowest_time
        cruise_speed = "{0:.6f}".format(cruise_speed)

        with open(file_out, 'a') as file_obj_out:
            file_obj_out.write("Case #{}: {}\n".format(str(case), cruise_speed))


if __name__ == '__main__':
    file_names = sys.argv[1:3]
    if not file_names:
        print('usage: [file_in] [file_out]')
    else:    
        main(*file_names)
