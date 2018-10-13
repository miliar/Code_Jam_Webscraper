# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 20:01:06 2017

@author: vanisas
"""
import math

#def give_max_min_(length, k, limit):
#    if length <= 1:
#        return k, 0, 0
##    elif (k == limit):
##        if (length % 2) == 0:
##            cell_max = length/2.0
##            cell_min = (length/2.0) - 1
##        else:
##            cell_max = math.floor(length/2.0)
##            cell_min = math.floor(length/2.0)
##        return k, cell_max, cell_min
#    else:
#        if (length % 2) == 0:
#            cell_max = length/2.0
#            cell_min = (length/2.0) - 1
#        else:
#            cell_max = math.floor(length/2.0)
#            cell_min = math.floor(length/2.0)
#        give_max_min(cell_max, k+1, limit)
#        give_max_min(cell_min, k+2, limit)
#
#
def give_max_min(length):
    if length == 0 :
        return 0, 0
    if (length % 2) == 0:
        cell_max = length/2.0
        cell_min = (length/2.0) - 1
    else:
        cell_max = math.floor(length/2.0)
        cell_min = math.floor(length/2.0)
    return cell_max, cell_min
   
def read_input(path_to_file):
    numbers_list = []
    people_list = []
    with open(path_to_file) as f:
        for idx, line in enumerate(f):
            if idx == 0:
                testcases = int(line)
#                print testcases
            else:
                numbers_list.append(int(line.split(' ')[0]))
                people_list.append(int(line.split(' ')[1]))
#        print numbers_list
#        print people_list
    return testcases, numbers_list, people_list


def write_output(number_list):
    output_file = open("poutsa_ksana.out", 'w')
    for idx, line in enumerate(number_list):
        output_file.write('Case #{0}: {1} {2}\n'.format(idx+1, number_list[idx][0], number_list[idx][1]))
    output_file.close()
    
   
def find_it(length_list, k):
#    length_list = map(int, list(str(length_list)))
#    print length_list
    if (math.log(k, 2)).is_integer():    
        level = int(math.log(k, 2))
        offset = 0
    else:
        level = int(math.log(k, 2))
        offset = k-(2**level)
#    print level
#    print offset
    k_list = []
    for i in range(level+1):  
        k_list = []
        for length in length_list:
            k_max, k_min = give_max_min(length)
            k_list.append(k_max)
            k_list.append(k_min)
#        print len(k_list)/2
        if i <> level :    
            k_list.sort(reverse=True)
        length_list = k_list[:]
#        print k_list
#    print len(k_list)
#    print 2*offset
#    print map(int, k_list[2*offset:(2*offset)+2])
    return map(int, k_list[2*offset:(2*offset)+2])
        
   
    
if __name__ == "__main__":
    result_list = []
    testcases, numbers_list, people_list = read_input('C-small-2-attempt0.in')
#    print testcases
#    print numbers_list
#    print people_list
#    print find_it([1000], 1)
#    print mymax, mymin
#    print mymax, mymin
    for i in range(testcases):
        result = find_it([numbers_list[i]], people_list[i])
        result_list.append(result)
    write_output(result_list)