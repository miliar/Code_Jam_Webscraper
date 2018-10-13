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
        N = int(file_line.replace('\n', ''))
        
        file_line = input_file.readline()
        file_line = file_line.replace('\n', '')
        list_of_quants = map(int, file_line.split())
        list_of_diffs = []
        list_of_pos_diffs = []
        for i in range(len(list_of_quants) - 1):
            diff = list_of_quants[i] - list_of_quants[i + 1]
            list_of_diffs.append(diff)
            if diff > 0:
                list_of_pos_diffs.append(diff)
        
        output_1 = np.sum(np.array(list_of_pos_diffs))
        output_2 = 0
        rate = np.max(np.array(list_of_diffs))
        for i in range(len(list_of_diffs)):
            output_2 += min(list_of_quants[i], rate)

        output_string = 'Case #' + str(case_num) + ': %d %d\n' % (output_1, output_2)

        output_file.write(output_string) ##
        print(output_string)
        case_num += 1
        
    output_file.close()











