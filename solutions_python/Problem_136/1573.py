#!/usr/bin/python
# -*- coding: utf-8 -*-

def solve_it(input_data):

    f = open('round1B.out', 'w')

    # parse the input
    lines = input_data.split('\n')

    num_of_case = int(lines[0])
    lines = lines[1:]

    for i in range(num_of_case):
        row = lines[i].split(' ')
        C = float(row[0])
        F = float(row[1])
        X = float(row[2])
        CPS = 2.0
        # print 'C: %f, F: %f, X: %f, Baseline: %f' % (C, F, X, baseline)

        total_time = 0.0

        current_t = 0.0

        while True:
            tmp1 = current_t + X/CPS
            current_t = current_t + C/CPS
            CPS += F
            tmp2 = current_t + X/CPS
            if tmp2 > tmp1:
                total_time = tmp1
                break

        # count = int(X/C)

        # if X<=C:
        #     total_time = baseline
        # else:
        #     for j in range(count-1):
        #         total_time += C/CPS
        #         CPS += F
        #     total_time += X/CPS

        #print total_time
        str_t = "%0.7f" % (total_time)
        f.write('Case #' + str(i+1) + ': ' + str_t + '\n')

    f.close()


    return None


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.'

