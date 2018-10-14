#!/usr/bin/python
#
# ./template.py -i template.inpt 
#

import math
from optparse import OptionParser

def parse_input(input_fname):
    input_arr = []
    f = open(input_fname, "r")

    # READ TESTCASE NUMBER
    testcase_num = int(f.readline())

    for t in range(0, testcase_num):
        ipt_strs = f.readline().split()
        tuple_ipt = (ipt_strs[0], int(ipt_strs[1]))
        input_arr.append((tuple_ipt))

    return input_arr

def write_output(output_fname, output_arr):
    f = open(output_fname, "w")
    for i in range(0, len(output_arr)):
        str_line = "Case #%d: %d\n" %(i+1, output_arr[i])
        f.write(str_line)
    f.close()

#non-recursive version
def powerset_v1(S):
    powerset = [[[], True]]
    if len(S) != 0:
        for i in range(0, len(S)):
            cur = S[i]
            new_member = []
            for c in powerset:
                n_mem = c[0] + [cur]
                if c[1]:
                    new_member.append([n_mem, True])

            for i in range(1, len(powerset)):
                powerset[i][1] = False
            powerset = powerset+new_member

    return powerset

def calculate_input(inpt):
    ipt_str = []
    for i in range(0, len(inpt[0])):
        ipt_str.append(inpt[0][i])

    n = inpt[1]
    count = 0

    all_cases = powerset_v1(ipt_str)
    for case in all_cases:
        arr_str = case[0]
        cur_n = 0
        for i in range(0, len(arr_str)):
            if arr_str[i] != 'a' and arr_str[i] != 'e' and arr_str[i] != 'i' and arr_str[i] != 'o' and arr_str[i] != 'u':
                cur_n = cur_n+1
            else:
                cur_n = 0

            if cur_n >= n:
                count = count+1
                break

    return count


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
