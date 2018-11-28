#!/usr/bin/python

import math
from optparse import OptionParser

result_arr = []

def parse_input(input_fname):
    input_arr = []
    f = open(input_fname, "r")

    # READ TESTCASE NUMBER
    testcase_num = int(f.readline())

    for i in range(0, testcase_num):
        ipt_strs = f.readline().split()
        assert(len(ipt_strs) == 2)
        input_arr.append(( int(ipt_strs[0]), int(ipt_strs[1]) ))

    return input_arr

def write_output(output_fname, output_arr):
    f = open(output_fname, "w")
    for i in range(0, len(output_arr)):
        str_line = "Case #%d: %d\n" %(i+1, output_arr[i])
        f.write(str_line)
    f.close()

def isPalindromes(n_int):
    if n_int <= 0:
        return False
    else:
        n_str = str(n_int)
        rev_n_str = n_str[::-1]

        return n_str == rev_n_str

def calculate_fairsquare(lower, upper):
    if(lower > upper):
        return 0
    else:
        # find lowest idx
        lower_idx = len(result_arr)
        for idx in range(0, len(result_arr)):
            if lower <= result_arr[idx]:
                lower_idx = idx
                break

        upper_idx = -1
        for idx in range(0, len(result_arr)):
            rev_idx = len(result_arr)-1-idx
            if upper >= result_arr[rev_idx]:
                upper_idx = rev_idx
                break;

        return max(0, upper_idx-lower_idx +1)

def main(input_fname, output_fname, u_limit):
    test_limit = int(math.ceil(math.sqrt(u_limit)))

    print ">>>>>>>> CALCULATE RESULT ARRAY"
    for i in range(1, test_limit):
        if isPalindromes(i):
            power_i = i*i
            if isPalindromes(power_i):
                result_arr.append(power_i)

    print "len(result_arr) : %d" %(len(result_arr))
    print result_arr

    print ">>>>>>>> READ_INPUT"
    input_arr = parse_input(input_fname)
    print "len(input_arr) : %d" %(len(input_arr))

    print ">>>>>>>> CALCULATE OUTPUT"
    output_arr = []
    for i in range(0, len(input_arr)):
        output_arr.append(calculate_fairsquare(input_arr[i][0], input_arr[i][1]))

    print ">>>>>>>> WRITE_OUTPUT"
    write_output(output_fname, output_arr)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u", type="int", dest="limit", default=int(1e14))
    parser.add_option("-i", type="str", dest="input_fname")

    (options, args) = parser.parse_args()
    if options.input_fname != None:
        i_fname = options.input_fname
        o_fname = options.input_fname + ".out"
        u_limit = options.limit

        print "INPUT FILE : %s" %(i_fname)
        print "OUTPUT FILE : %s" %(o_fname)
        print "UPPER LIMIT : %d" %(u_limit)

        main(i_fname, o_fname, u_limit)
