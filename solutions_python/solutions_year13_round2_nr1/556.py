'''
Created on Apr 1, 2013

@author: pawel
'''
import sys
import math, time
 
def read_case_info(file):
    data = {}
    raw_line = file.readline().strip('\n').split(' ')
    data['armin_mote'] = int(raw_line[0])
    data['number_of_motes'] = int(raw_line[1])
    motes = [int(mote) for mote in file.readline().strip('\n').split(' ')]
    data['motes'] = sorted(motes) 
    return data

def get_number_of_modifications(armin_mote, start, motes):
    end_index = len(motes)
    while start < end_index:
        if armin_mote > motes[start]:
            armin_mote += motes[start]
            start += 1
        else:
            #changing part
            motes_copy = motes[:]
            motes_copy.pop()
            if len(motes_copy) == 0:
                return 1;
            by_removing = get_number_of_modifications(armin_mote, start, motes_copy)
            new_armin_mote = armin_mote + armin_mote - 1
            if new_armin_mote <= armin_mote:
                by_adding = float('inf')
            else:
                by_adding = get_number_of_modifications(new_armin_mote, start, motes)
            return min(by_adding, by_removing) + 1
    return 0
                
def solve_case(data):
    return get_number_of_modifications(data['armin_mote'], 0, data['motes'])

file = open(sys.argv[1], 'r')
number_of_cases = int(file.readline().strip())
counter = 0
results = []
while number_of_cases > counter:
    case_info = read_case_info(file)
    results.append(solve_case(case_info))
    counter += 1
    
file_output = open(sys.argv[2], 'w')
for index, result in enumerate(results):
    file_output.write('Case #' + str(index + 1) +  ': ' + str(result) + '\n') 
