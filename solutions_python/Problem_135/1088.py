f = open('A-small-attempt0.in','r')
input_file = [x.strip().split() for x in f.readlines()]
f.close()

#number of cases
nC = int(input_file[0][0])

#number of lines per case
nL = 10
cases = []
for idx in range(nC):
    jdx = idx*nL+1
    #row selections, adjusted to index from 0
    row_1 = int(input_file[jdx][0])-1
    row_2 = int(input_file[jdx+5][0])-1
    matrix_1 = [ [int(x) for x in y] for y in input_file[jdx+1:jdx+5]]
    matrix_2 = [ [int(x) for x in y] for y in input_file[jdx+6:jdx+10]]
    rows = [row_1,row_2]
    matrices = [matrix_1,matrix_2]
    cases.append([rows,matrices])

def solve_case(case):
    rows,matrices = case
    relevant_rows = [set(x[idx]) for x,idx in zip(matrices,rows)]
    common_elements = set.intersection(*relevant_rows)
    if len(common_elements) == 1:
        solution = str(list(common_elements)[0])
    elif len(common_elements) == 0:
        solution = 'Volunteer cheated!'
    elif len(common_elements) > 1:
        solution = 'Bad magician!'
    return solution


f = open('A_small_solution.txt', 'w')    
for case_idx,case in enumerate(cases):
    f.write('Case #' + str(case_idx+1)+ ': ' + solve_case(case) +'\n')
f.close()
