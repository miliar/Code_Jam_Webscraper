#!/usr/bin/python

import math
from optparse import OptionParser

INITIAL_G = 100

def parse_input(input_fname):
    input_arr = []
    f = open(input_fname, "r")

    # READ TESTCASE NUMBER
    testcase_num = int(f.readline())

    for t in range(0, testcase_num):
        ipt_strs = f.readline().split()
        assert(len(ipt_strs) == 2)

        ipt_m       = int(ipt_strs[0])
        ipt_n       = int(ipt_strs[1])

        ipt_cutgrass   = []

        for row in range(0, ipt_m):
            c_row_str = f.readline().split()
            assert(len(c_row_str) == ipt_n)
            c_row = [INITIAL_G - int(s) for s in c_row_str]
            ipt_cutgrass.append(c_row)

        tuple_inpt = (ipt_m, ipt_n, ipt_cutgrass)
        input_arr.append(tuple_inpt)

    return input_arr

def write_output(output_fname, output_arr):
    f = open(output_fname, "w")
    for i in range(0, len(output_arr)):
        if output_arr[i]:
            str_line = "Case #%d: %s\n" %(i+1, "YES")
        else:
            str_line = "Case #%d: %s\n" %(i+1, "NO")
        f.write(str_line)
    f.close()

def calculate_input(inpt):
    m           = inpt[0]
    n           = inpt[1]
    cut_grass   = inpt[2]

    row_cancut  = [0 for i in range(0, m)]
    col_cancut  = [0 for i in range(0, n)]

    # Calculate cancut
    for r in range(0, m):
        row_cancut[r] = min(cut_grass[r])

    for c in range(0, n):
        col_cancut[c] = min([cut_grass[r][c] for r in range(0, m)])

    # Try cutting
    cancut = True
    for r in range(0, m):
        for c in range(0, n):
            elem = cut_grass[r][c]
            if elem > max(row_cancut[r], col_cancut[c]):
                cancut = False

    return cancut

def main(input_fname, output_fname):
    print ">>>>>>>> READ_INPUT"
    input_arr = parse_input(input_fname)
    print "len(input_arr) : %d" %(len(input_arr))
    #print input_arr

    print ">>>>>>>> CALCULATE OUTPUT"
    output_arr = []
    for i in range(0, len(input_arr)):
        output_arr.append(calculate_input(input_arr[i]))

    print ">>>>>>>> WRITE_OUTPUT"
    write_output(output_fname, output_arr)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", type="str", dest="input_fname")

    (options, args) = parser.parse_args()
    if options.input_fname != None:
        i_fname = options.input_fname
        o_fname = options.input_fname + ".out"

        print "INPUT FILE : %s" %(i_fname)
        print "OUTPUT FILE : %s" %(o_fname)

        main(i_fname, o_fname)
