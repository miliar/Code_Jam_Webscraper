import numpy as np
import math
import time


input_file_name = './A-large.in'
output_file_name = './A-large.out'
    

if __name__ == '__main__':

    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')

    # get info from input file
    file_line = input_file.readline()
    file_line = file_line.replace('\n', '')
    num_cases = int(file_line)

    case_num = 1
    while True:
        file_line = input_file.readline()
        if file_line == '' or file_line == '\n':
            input_file.close()
            break
        file_line = file_line.replace('\n', '')
        file_line_list = file_line.split()
        N = int(file_line_list[0])
        X = int(file_line_list[1])      

        file_line = input_file.readline()
        file_line = file_line.replace('\n', '')
        file_line_list = file_line.split()
        disc_list = map(int, file_line_list)

        disc_list.sort()

        small_i = 0
        big_i = N - 1
        num_discs = 0

        if N == 1:
            num_discs = 1
        else:
            while True:
                if small_i == big_i:
                    num_discs += 1
                    break
                if small_i > big_i:
                    break
                if disc_list[big_i] + disc_list[small_i] <= X:
                    small_i += 1
                    big_i -= 1
                    num_discs += 1
                else:
                    big_i -= 1
                    num_discs += 1
                
               

        output_string = 'Case #' + str(case_num) + ': ' + str(num_discs) + '\n'

        output_file.write(output_string) ##
        print(output_string)
        case_num += 1
        
    output_file.close()











