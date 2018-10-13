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
        line1 = f.readline().split()
        line2 = f.readline().rstrip('\n')
        input_arr.append([int(line1[0]), int(line1[1]), line2])

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

def multiplyChar(char1, char2):
    if char1[1] == "1":
        mul_sign = char2[0]
        mul_char = char2[1]
    elif char1[1] == "i":
        if char2[1] == "1":
            mul_sign = 1;
            mul_char = "i"
        elif char2[1] == "i":
            mul_sign = -1;
            mul_char = "1"
        elif char2[1] == "j":
            mul_sign = 1;
            mul_char = "k"
        elif char2[1] == "k":
            mul_sign = -1;
            mul_char = "j"
        else:
            assert(False)
    elif char1[1] == "j":
        if char2[1] == "1":
            mul_sign = 1;
            mul_char = "j"
        elif char2[1] == "i":
            mul_sign = -1;
            mul_char = "k"
        elif char2[1] == "j":
            mul_sign = -1;
            mul_char = "1"
        elif char2[1] == "k":
            mul_sign = 1;
            mul_char = "i"
        else:
            assert(False)
    elif char1[1] == "k":
        if char2[1] == "1":
            mul_sign = 1;
            mul_char = "k"
        elif char2[1] == "i":
            mul_sign = 1;
            mul_char = "j"
        elif char2[1] == "j":
            mul_sign = -1;
            mul_char = "i"
        elif char2[1] == "k":
            mul_sign = -1;
            mul_char = "1"
        else:
            assert(False)
    else:
        assert(False)
    return [mul_sign*char1[0]*char2[0], mul_char];

def isEqual(char1, char2):
    return (char1[0] == char2[0]) and (char1[1] == char2[1])

def getChar(i, strl):
    char = strl[i%len(strl)]
    return [1, char]

def calculate_input(inpt):
    L    = inpt[0]
    X    = inpt[1]
    strl = inpt[2]

    # 0 = searching for i
    # 1 = searching for j
    # 2 = searching for k
    # 3 = ijk are found
    cur_state   = 0;
    cur_accum   = [1, "1"]
    cur_char_th = 0

    while cur_char_th < L*X:
        cur_char = getChar(cur_char_th, strl)

        cur_accum = multiplyChar(cur_accum, cur_char)
        #print cur_char_th, cur_char, cur_accum

        if cur_state < 3:
            target_char = None
            if cur_state == 0:
                target_char = [1, "i"]
            elif cur_state == 1:
                target_char = [1, "j"]
            elif cur_state == 2:
                target_char = [1, "k"]
            else:
                assert(False)

            if isEqual(cur_accum, target_char):
                cur_state  += 1
                cur_accum   = [1, "1"]

        cur_char_th +=1

    assert(cur_char_th == L*X)
    #print cur_accum, cur_state
    if cur_state == 3 and isEqual(cur_accum, [1, "1"]):
        return True
    else:
        return False

def main(input_fname, output_fname):
    print ">>>>>>>> READ_INPUT"
    input_arr = parse_input(input_fname)
    print "len(input_arr) : %d" %(len(input_arr))
    #print input_arr

    print ">>>>>>>> CALCULATE OUTPUT"
    output_arr = []
    for i in range(0, len(input_arr)):
    #for i in range(0, 5):
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
