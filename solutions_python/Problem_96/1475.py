'''
Created on 14.04.2012

@author: Marco
'''

def read_file(adress):
    read_index = []
    f = open(adress, 'r')
    for line in f:
        read_index.append(line)
    f.close()
    index = []
    for entry in read_index[1:]:
        integer_strings = entry.split()
        integer_list = []
        for i in integer_strings:
            integer_list.append(int(i))
        index.append(integer_list)
    return index

def write_file(return_list, adress):
    case = 1
    f = open(adress, 'w')
    for value in return_list:
        write_line = 'Case #'+ str(case)+': '+str(value)+'\n'
        f.write(write_line)
        case = case + 1
    f.close()

def calculate(result_list):
    return_list = []
    count = 0
    for single_list in result_list:
        googlers = single_list[0]
        surprising_triplets = single_list[1]
        p = single_list[2]
        total_points = single_list[3:]
        normal_minimum_points = p+(2*(p-1))
        surprising_minimal_points = normal_minimum_points - 2
        if surprising_minimal_points < 1:
            surprising_minimal_points = 1
        for points in total_points:
            if points >= normal_minimum_points:
                count = count + 1
            elif points >= surprising_minimal_points and surprising_triplets > 0:
                count = count + 1
                surprising_triplets = surprising_triplets - 1
        return_list.append(count)
        count = 0
    return return_list

read_list = read_file('C:/Users/Marco/Desktop/B-large.in')
result_list = calculate(read_list)
write_file(result_list, 'C:/Users/Marco/Desktop/B-large.out')
