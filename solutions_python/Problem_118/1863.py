'''
Created on Apr 1, 2013

@author: pawel
'''
import sys
import math
 
def read_case_info(file):
    data = {}
    raw_line= file.readline().strip('\n').split(' ')
    data['start'] = int(raw_line[0])
    data['end'] = int(raw_line[1])
    return data

def is_palindrome(number):
    str_number = str(number)
    if str_number == str_number[::-1]:
        return True
    return False

def solve_case(data):
    counter = 0
    start = int(math.ceil(math.sqrt(data['start'])))
    for i in range(start, data['end'] + 1):
        if is_palindrome(i):
            number = i**2
            if number <= data['end'] and is_palindrome(number):
                counter += 1
    return str(counter)

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
    file_output.write('Case #' + str(index + 1) +  ': ' + result + '\n') 
