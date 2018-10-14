'''
Google Code Jam 2012, Qualification Round
Problem C
Created on Apr 13, 2012

@author: Gabriel D. Holodak
'''
import math
fin = open('C-large.in')
fout = open('output.txt', 'w')
num_cases = int(fin.readline().strip())
memo_dictionary = dict()
def all_possible_pairs(n):
    if n in memo_dictionary:
        return memo_dictionary.get(n)
    else:
        pairs = []
        num_as_str = str(n)
        for index in range(len(str(n))):
            num = int(num_as_str[index:] + num_as_str[:index])
            if not(num in pairs or num <= n):
                pairs.append(num)
        memo_dictionary[n]=pairs
        return pairs
def num_pairs(n, B):
    all_pairs = all_possible_pairs(n)
    valid_pairs = []
    for pair_being_tested in all_pairs:
        if pair_being_tested <= B:
            valid_pairs.append(pair_being_tested)
    #if len(valid_pairs) != 0:
        #print 'For', n, 'valid pairs are', valid_pairs
    return len(valid_pairs)
for i in range(num_cases):
    output_string = 'Case #' + str(i + 1) + ": "
    print 'Case #' + str(i + 1) + ":",
    limits = fin.readline().strip().split()
    A = int(limits[0])
    B = int(limits[1])
    pair_possibilities = 0
    for index in range(A, B):
        pair_possibilities += num_pairs(index, B)
    #print pair_possibilities
    fout.write(output_string + str(pair_possibilities) + '\n')
fout.close()
fin.close()
