
import sys
import collections

import numpy as np

#For debugging.
from IPython.Shell import IPShellEmbed
ipshell = IPShellEmbed()

if len(sys.argv) < 2:
    print('Need an input file!')
    exit()

input_filename = sys.argv[1]
output_filename = input_filename[:-3] + '.out'

input_file = file(input_filename)
output_file = file(output_filename,'w')

num_cases = int(input_file.readline())



for i in xrange(num_cases):
    #Parse something like this :
    #'4 O 2 B 1 B 2 O 4\n'
    line = input_file.readline().split(' ')
    #remove trailing newline
    line[-1] = line[-1][:-1]
    
    num_combinations = int(line[0])
    combinations = [(c[0:2],c[-1]) for c in line[1:1+num_combinations]]
    num_oppositions = int(line[1+num_combinations])
    oppositions = line[2+num_combinations:2+num_combinations+num_oppositions]
    num_invokes  = int(line[2+num_combinations+num_oppositions])
    invokes = line[3+num_combinations+num_oppositions]
    
    elements = []
    for inv in invokes:
        elements.append(inv)
        
        if len(elements) >= 2:
            last_two = ''.join(elements[-2:])
            for comb in combinations:
                if (last_two.find(comb[0]) != -1
                 or last_two.find(comb[0][::-1]) != -1):
                    elements.pop()
                    elements.pop()
                    elements.append(comb[1])
                    
            elements_str = ''.join(elements)
            for opp in oppositions:
                find_all = True
                for letter in opp:
                    if elements_str.find(letter) == -1:
                        find_all = False
                        break
                if find_all:
                    elements = []
    
    output_file.write('Case #%i: ['%(i+1))
    for el in elements[:-1]:
        output_file.write('%s, '%(el))
    if len(elements) > 0:
        output_file.write('%s]\n'%(elements[-1]))
    else:
        output_file.write(']\n')
        
