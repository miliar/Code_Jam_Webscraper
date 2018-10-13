'''
Created on 11-Apr-2015

@author: rohinton
'''

import sys

def calculate_friends(audience):
    friends = 0
    current_shyness = 0
    current_standing = 0
    for audience_set in audience:
        if audience_set > 0 and current_standing < current_shyness:
            increase = (current_shyness - current_standing)
            friends = friends + increase
            current_standing = current_standing + increase
        current_standing = current_standing + audience_set
        current_shyness = current_shyness + 1    
            
    return friends

if __name__ == '__main__':
    test_case_file = sys.argv[1]
    input_file = open(test_case_file)
    test_case_count = int(input_file.readline())
    output = []
    
    for i in range(test_case_count):
        test_case = input_file.readline()
        test_case = test_case[0:len(test_case) - 1]
        audience_index = test_case.find(' ') + 1
        audience = []
        for audience_set in test_case[audience_index:]:
            audience.append(int(audience_set))
        friends = calculate_friends(audience)
        output.append('Case #' + str(i + 1) + ': ' + str(friends))
        
    input_file.close()
        
    output_file = open('output.out', 'w')
    for output_line in output:
        output_file.write(output_line + '\n')
        
    output_file.close() 