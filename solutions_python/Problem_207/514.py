#!/usr/bin/python

def solve(uni_c, r_c, o_c, y_c, g_c, b_c, v_c):
    last_l = "X"
    result = ""
    order = ["r", "y", "b"]
    first = True
    while uni_c > 0:
        #print "total: " + str(uni_c)
        #print "r: " + str(r_c)
        #print "y: " + str(y_c)
        #print "b: " + str(b_c)
        max_l = "X"
        max_c = 0
        for l in order:
            if l == "r":
                if r_c > max_c and last_l != "R":
                    max_c = r_c
                    max_l = "R"
            if l == "y":
                if y_c > max_c and last_l != "Y":
                    max_c = y_c
                    max_l = "Y"
            if l == "b":
                if b_c > max_c and last_l != "B":
                    max_c = b_c
                    max_l = "B"

        if max_l == "X":
            #print "error 1111111111111111111111!!!!!!!!!!!!!!!!!!!!!!!!!"
            return "IMPOSSIBLE"

        result += max_l
        uni_c -= 1
        if max_l == "R":
            r_c -= 1
            last_l = "R"
            if first:
                first = False
                order = ["r", "y", "b"]
        if max_l == "Y":
            y_c -= 1
            last_l = "Y"
            if first:
                first = False
                order = ["y", "b", "r"]
        if max_l == "B":
            b_c -= 1
            last_l = "B"
            if first:
                first = False
                order = ["b", "r", "y"]

    if result[0] == result[-1]:
        #print "error 222222222222222222!!!!!!!!!!!!!!!!!!!!!!!!!!"
        return "IMPOSSIBLE"
    return result

import sys
input_lines = open(sys.argv[1], "rt").readlines()
stripped_input_lines = [line.strip() for line in input_lines]
num_tests = int(input_lines[0])
#print num_tests

i=1
current_line = 1
while len(stripped_input_lines) > current_line:
    #print "new test!!!!!!!!!!!"
    test_line = stripped_input_lines[current_line]
    #print test_line
    uni_c = int(test_line.split()[0])
    r_c = int(test_line.split()[1])
    o_c = int(test_line.split()[2])
    y_c = int(test_line.split()[3])
    g_c = int(test_line.split()[4])
    b_c = int(test_line.split()[5])
    v_c = int(test_line.split()[6])
    current_line += 1
    result = solve(uni_c, r_c, o_c, y_c, g_c, b_c, v_c)
    print "Case #"+str(i)+": "+str(result)
    i+=1
