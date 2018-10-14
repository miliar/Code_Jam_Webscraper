#INPUT PARSING
f = open('B-large.in','r')
input_file = [x.strip() for x in f.readlines()]
f.close()

n_cases = int(input_file.pop(0))
input_cases = []

while len(input_file)>0:
    N,M = [int(x) for x in input_file[0].split()]
    lawn = [ [int(x) for x in y.split()] for y in input_file[1:N+1]]
    input_file = input_file[N+1:]
    input_cases.append(lawn)
    
#SOLVE PROBLEM

def solve_problem(lawn):
    for i,row in enumerate(lawn):
        for j,aij in enumerate(row):
            strict_row_min = False
            strict_col_min = False    
            for x in row:
                if x > aij:
                    strict_row_min = True
            for x in [en_row[j] for en_row in lawn]:
                if x > aij:
                    strict_col_min = True
            if strict_row_min and strict_col_min:
                return 'NO'
    return 'YES'
    
#OUTPUT SOLUTIONS

f = open('B_large_solution.txt','w')
for i,x in enumerate(input_cases):
    f.write('Case #' + str(i+1) + ': ' + solve_problem(x) + '\n')
f.close()