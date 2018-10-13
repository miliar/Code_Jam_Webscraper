#!/usr/bin/python

import math

def solve(avail_c, ordered_c, panks):
    best_res = 0
    for i in xrange(len(panks)):
        curr_res = 0
        pank = panks[i]
        main_r = pank["radius"]
        main_h = pank["height"]
        #print "main_r: " + str(main_r)
        #print "main_h: " + str(main_h)
        rest_panks = panks[:i] + panks[i + 1:]
        relevant_panks = [pank for pank in rest_panks if pank["radius"] <= main_r]
        if len(relevant_panks) < ordered_c - 1:
            continue
        #print "relevant_panks: " + str(relevant_panks)
        relevant_rhs = [pank["radius"] * pank["height"] for pank in relevant_panks]
        relevant_rhs.sort(reverse=True)
        curr_sum = 0
        for j in xrange(len(relevant_rhs)):
            if j >= ordered_c - 1:
                break
            #print "adding rh: " + str(relevant_rhs[j])
            curr_sum += relevant_rhs[j]
        curr_sum += main_r * main_h
        #print "curr_sum: " + str(curr_sum)
        curr_res = (curr_sum * 2 + main_r * main_r) * math.pi
        #print "curr_res: " + str(curr_res)
        if curr_res > best_res:
            best_res = curr_res
    return best_res

import sys
input_lines = open(sys.argv[1], "rt").readlines()
stripped_input_lines = [line.strip() for line in input_lines]
num_tests = int(input_lines[0])
#print num_tests

i=1
current_line = 1
while len(stripped_input_lines) > current_line:
    #print "new test!!!!!!!!!!!"
    panks = []
    test_line = stripped_input_lines[current_line]
    #print test_line
    avail_c = int(test_line.split()[0])
    ordered_c = int(test_line.split()[1])
    current_line += 1
    current_test_line = 0
    while current_test_line < avail_c:
        test_line = stripped_input_lines[current_line + current_test_line]
        radius = int(test_line.split()[0])
        height = int(test_line.split()[1])
        pank = {"radius" : radius, "height" : height}
        panks.append(pank)
        current_test_line += 1
        #print test_line
    current_line += avail_c
    result = solve(avail_c, ordered_c, panks)
    print "Case #"+str(i)+": "+str(result)
    i+=1
