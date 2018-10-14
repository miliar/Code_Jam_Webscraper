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

#############################################################################

# file_in = 'sample.in'
file_in = 'A-small-attempt1.in'
# file_in = 'A-large.in'

filename, _ = os.path.splitext(file_in)
file_out = filename + '.out'

lines_in = read_lines(file_in)
num_cases = int(lines_in[0])


#############################################################################
lines_out = []

for ind in range(num_cases):

    row0 = int(lines_in[1 + ind * 10]) - 1
    row1 = int(lines_in[6 + ind * 10]) - 1

    # print row0
    # print row1

    mat0 = take_mat(2 + ind * 10, lines_in)
    mat1 = take_mat(7 + ind * 10, lines_in)

    
    # print mat0
    # print mat1


    # num_flag = len(set(mat0[row0] + mat1[row1]))

    num_inter = len(mat0[row0].intersection(mat1[row1]))

    if num_inter == 0:
        lines_out.append("Case #%d: %s\n" % (ind + 1, "Volunteer cheated!"))

    if num_inter == 1:
        lines_out.append("Case #%d: %d\n" % (ind + 1, list(mat0[row0].intersection(mat1[row1]))[0]))

    if num_inter > 1:
        lines_out.append("Case #%d: %s\n" % (ind + 1, "Bad magician!"))


write_lines(lines_out, file_out)






#############################################################################



# lines_out = []
# for ind in range(num_cases):
#     lines_out.append("Case #%d:\n" % (ind + 1))
# write_lines(lines_out, 'test.out')