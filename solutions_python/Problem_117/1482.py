'''
Created on Apr 1, 2013

@author: pawel
'''
import sys
 
def read_case_info(file):
    data = {}
    raw_line= file.readline().strip('\n').split(' ')
    data['rows'] = int(raw_line[0])
    data['cols'] = int(raw_line[1])
    data['pattern'] = {}
    for i in range(data['rows']):
        raw_line2 = file.readline().strip('\n').split(' ')
        for j in range(data['cols']):
            data['pattern'][(i,j)] = raw_line2[j]
    return data

def get_max_decorator(t, data):
    mem = {}
    if t == 'row':
        size = data['cols']
    else:
        size = data['rows']
    def get_max(index):
        try:
            return mem[index]
        except:
            pass
        max = 0
        for i in range(size):
            if t == 'row':
                value = data['pattern'][(index, i)]
            else:
                value = data['pattern'][(i, index)]
            if value > max:
                max = value 
        mem[index] = max
        return mem[index]
    return get_max

def solve_case(data):
    get_row_max = get_max_decorator('row', data)
    get_col_max = get_max_decorator('col', data)
    for key, value in data['pattern'].items():
        row_max = get_row_max(key[0])
        col_max = get_col_max(key[1])
        if row_max > value and col_max > value:
            return 'NO'
    return 'YES'

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
