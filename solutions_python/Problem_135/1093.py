__author__ = 'narun'
import itertools

def write_output(fh, case, output_list):
    fh.write('Case #'+str(case)+': '+''.join(output_list)+'\n')


filename = 'A-small-attempt0.in'
outfile = 'A-small-attempt0.out'
# filename = 'A-large.in'
# outfile = 'A-large.out'
input_file = open(filename, 'r')
output_file = open(outfile, 'w')
debug = False

num = int(input_file.readline())
for i in range(num):
    first = int(input_file.readline())
    print(first) if debug else None
    row = {str(x): 0 for x in range(1,17)}
    print(row, len(row)) if debug else None
    for k in range(4):
        if k == first-1:
            for x in input_file.readline().split():
                row[x] += 1
                print(x) if debug else None
        else:
            input_file.readline()
    print(row) if debug else None
    second = int(input_file.readline())
    print(second) if debug else None
    answer = list()
    for k in range(4):
        if k == second-1:
            for x in input_file.readline().split():
                row[x] += 1
                if row[x] > 1:
                    answer.append(x)
                print(x) if debug else None
        else:
            input_file.readline()
    print(answer) if debug else None
    if len(answer) == 0:
        write_output(output_file, i+1, ['Volunteer cheated!'])
    elif len(answer) == 1:
        write_output(output_file, i+1, answer)
    elif len(answer) > 1:
        write_output(output_file, i+1, ['Bad magician!'])