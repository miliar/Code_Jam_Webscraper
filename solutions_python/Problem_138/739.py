#!/usr/bin/env pypy
import sys, os

outfile = open("%s.out" % sys.argv[1], "w")
case_number = 1

# def finder(goal, liste):
#     l = len(liste)
#     if l == 0:
#         print "fail"
#         return
#     else:
#         if liste[-1] < goal:
#             return
#         else:
            
        
        

def solving(case):
    global case_number
    # print case
    
    naomi, ken = map(sorted, case)
    naomi_i = naomi[::-1]
    ken_n   = [a for a in ken]
    # print naomi, ken
    
    naomi_normal_counter = 0
    naomi_cheated_counter = 0
    
    for n_block in naomi_i:
        ken_found = ken[0]
        for k_block in ken:
            if k_block > n_block:
                ken_found = k_block
                break
        index = ken.index(ken_found)
        ken = ken[:index] + ken[index + 1:]
        if ken_found < n_block:
            naomi_normal_counter += 1
    
    for n_block in naomi:
        if n_block < ken_n[0]:
            ken_n = ken_n[:-1]
        else:
            naomi_cheated_counter += 1
            ken_n = ken_n[1:]
        
    result = "Case #%d: %d %d" % (case_number, naomi_cheated_counter, naomi_normal_counter)
    # print result
    outfile.write(result + '\n')
    case_number += 1
    # print ""
    
with open(sys.argv[1]) as infile:
    for index, l in enumerate(infile.readlines()[1:]):
        if index % 3 == 0:
            pass
        else:
            numbers = map(float, l.split())
            if index % 3 == 1:
                case = [numbers]
            else:
                case.append(numbers)
                solving(case)    
outfile.close()
