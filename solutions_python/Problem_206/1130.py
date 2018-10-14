import os
import sys
import itertools


def output_format(string_number,test_case):
    output = "Case #%d:" % (test_case+1)
    output += " %s" % str(string_number)
    output +="\n"
    return output


if __name__ == "__main__":
    f = open("A-large.in",'r')
    # f = open("/home/mike/Desktop/codejam/A-large.in", 'r')
    test_cases = int(f.readline())
    out = open("/home/mike/Desktop/codejam/results_A_large.txt", 'w')

    # print test_cases
    for i in range(test_cases):
        input = f.readline().strip("\n")
        D, H = input.split(' ')
        D, H = (int(D), int(H))
        slowest_time = 0.0
        for j in range(H):
            horse_start, speed = f.readline().strip('\n').split(' ')
            # print horse_start, speed
            dest_time = (D - int(horse_start))/float(speed)
            if dest_time >= slowest_time:
                slowest_time = dest_time

        result = str(D/slowest_time)
        output = output_format(result, i)
        out.write(output)


