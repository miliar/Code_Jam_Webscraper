import sys
import time
import os


def read_lines(file_in):
    with open(file_in) as f:
        content = f.read()
    lines_in = content.splitlines()
    return lines_in


def write_lines(lines_out, file_out):
    with open(file_out, 'w') as f:
        f.writelines(lines_out)


def take_mat(bgn, lines_in):
    mat = []
    for ind in range(4):
        mat.append(set(map(int, lines_in[ind + bgn].split(' '))))
    return mat

# #####################

# file_in = 'A-toy.in'
# file_out = 'A-toy.out'
# file_in = 'A-small-attempt0.in'
# file_out = 'A-small-attempt0.out'
file_in = 'A-large.in'
file_out = 'A-large.out'

lines_in = read_lines(file_in)

num_line = int(lines_in[0])

list_max_shy = []
list_need = []
list_out = []

for ind in range(1, len(lines_in)):
    part_1, part_2 = lines_in[ind].split(' ')
    list_max_shy.append(int(part_1))
    list_num_each_level = [int(item) for item in part_2]
    # list_list_num.append()

    list_need_each_level = [bool(list_num_each_level[level]) * (level -
                                                                sum(list_num_each_level[0:level]))
                            for level in range(len(list_num_each_level))]

    # list_need.append(max(list_need_each_level))

    list_out.append('Case #{}: {}\n'.format(ind, max(list_need_each_level)))
##########################

list_out[-1] = list_out[-1][:-1]
write_lines(list_out, file_out)
