#!/usr/bin/env python

RES_YES = "YES"
RES_NO = "NO"

def check_horiz(value, row, MATRIX):
    for cell in MATRIX[row]:
        if cell > value:
            return False
    return True;

def check_vertic(value, col, MATRIX, N):
    row = 0
    while row < N:
        if MATRIX[row][col] > value:
            return False
        row += 1
    
    return True

def solve(probleminput):
    """
    in: expects a list of inputs for the current testcase. see NUM_OF_ELEMENTS_PER_PROBLEM for the list size
    out: should return the solution for this testcase
    """
    (N, M) = [ int(x) for x in probleminput[0].split(' ')]
    MATRIX = [x.split(' ') for x in probleminput[1:]]
    
    # now check each cell
    for col in range(M):
        for row in range(N):
            # each cell must be reachable with a horizontal 
            # of vertical line of the same grass height
            if not check_horiz(MATRIX[row][col], row, MATRIX) and not check_vertic(MATRIX[row][col], col, MATRIX, N):
                return RES_NO;
    
    return RES_YES

###### program skeleton #######
import sys
problem = [l.replace('\n', '') for l in sys.stdin.readlines()]
num_of_problems = 0
num_of_lines_per_problem = 0
problem_lines = []
testcase = 1
for num, line in enumerate(problem):
    if num == 0:
        num_of_problems = int(line)
        continue
    
    if len(problem_lines) == 0:
        num_of_lines_per_problem = int(line.split(' ')[0])
    
    problem_lines.append(line)

    if len(problem_lines) == num_of_lines_per_problem + 1:
        result = solve(problem_lines)
        print "Case #%i: %s" % (testcase, result)
        problem_lines = []
        testcase += 1
