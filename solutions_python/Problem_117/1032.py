
import sys
import os

import numpy as np


filename = sys.argv[1]

input_file = open(filename, 'r')
output_file = open(os.path.splitext(filename)[0] + '.out', 'w')

input_lines = input_file.readlines()
num_lawns = int(input_lines[0])

next_line = 1
for l in range(num_lawns):
    #first line is dimensions
    dim_str = input_lines[next_line].strip('\n').split(' ')
    m, n = int(dim_str[0]), int(dim_str[1])

    #then extract the a_ij matrix
    next_line += 1
    lawn = [input_lines[next_line + xi].strip('\n').split(' ') for xi in range(m)]
    lawn = np.array(lawn, dtype=int)
    next_line += m

    lawn_cols = lawn.T
    #We'll invalidate impossible layouts, rather than look for a solution
    #for each lawn.
    result = 'YES'
    for i, row_i in enumerate(lawn):
        row_max = np.max(row_i)
        #When a row contains a higher grass than the rest, it means it was cut column-wise,
        #so we'll check that column to see if it was possible.
        cols_to_check = np.where(row_i < row_max)[0]
        max_value_for_column = row_i[cols_to_check]
        for j, possible_max in zip(cols_to_check, max_value_for_column):
            col_j = lawn_cols[j]
            if np.max(col_j) > possible_max:
                result = 'NO'
                break

    output_file.write('Case #%i: %s\n' % (l + 1, result))

output_file.close()
