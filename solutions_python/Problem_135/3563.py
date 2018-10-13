import sys, itertools

input_file_name = 'input1.in'
output_file_name = 'output1.txt'

f_in = open(input_file_name,'r')
f_out = open(output_file_name,'w')

contents = f_in.readlines()
num_cases = int(contents.pop(0))
for case in range (num_cases):
    table1 = []
    table2 = []
    rowguess1 = int(contents.pop(0)) - 1
    for i in range(4):
        row = contents.pop(0)
        x = row.split()
        table1.append([int(i) for i in x])
    rowguess2 = int(contents.pop(0)) - 1
    for i in range(4):
        row = contents.pop(0)
        x = row.split()
        table2.append([int(i) for i in x])
    intersection = [val for val in table1[rowguess1] if val in table2[rowguess2]]
    if len(intersection) == 1:
        print('Case #{}: {}'.format(case+1, intersection[0]), file = f_out)   
    elif len(intersection) == 0:
        print('Case #{}: {}'.format(case+1, 'Volunteer cheated!'), file = f_out)   
    else:
        print('Case #{}: {}'.format(case+1, 'Bad magician!'), file = f_out)
  
f_in.close()
f_out.close()
