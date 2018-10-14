import os
import sys
import pdb

os.chdir(os.path.dirname(os.path.abspath(__file__)))

input_file = open('input.txt')
input = input_file.read().split('\n')
input_file.close()

T = eval(input[0])
input = input[1:]

possibility = []

for case in range(0,T):
    poss = True
    N,M = map(lambda x:eval(x), input[0].split(' '))
    input = input[1:]
    lawn = []
    for line_no in range(0,N):
        lawn += [map(lambda x:eval(x),input[0].split(' '))]
        input = input[1:]
    for x_cor in range(0,N):
        for y_cor in range(0,M):
            counter = 0
            try:
                if filter(lambda x:x>lawn[x_cor][y_cor],lawn[x_cor]):
                    counter += 1
            except:
                pdb.set_trace()
            try:
                if filter(lambda x:x>lawn[x_cor][y_cor],map(lambda x:x[y_cor],lawn)):
                    counter += 1
            except:
                pdb.set_trace()
            if counter > 1:
                poss=False
                break
        if not poss:
            break
    possibility += [poss]


output_file = open('output.txt','w')
for case in range(0,T):
    output = 'Case #'+str(case+1)+': '
    if possibility[case]:
        output += 'YES\n'
    else:
        output += 'NO\n'
    output_file.write(output)
output_file.close()