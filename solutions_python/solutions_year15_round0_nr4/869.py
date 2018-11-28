import io
import heapq
from collections import deque

def read_input(filepath):
    with open(filepath, 'r') as f:
        content = f.read().splitlines()
    return content

def write_output(filepath, answers):
    with open(filepath, 'w') as f:
        for i in range(len(answers)):
            print 'Case #' + str(i+1) + ': ' + answers[i]
            f.write('Case #' + str(i+1) + ': ' + answers[i] + '\n')

'''for each test case'''
def run_each(case):
    X, R, C = int(case.split()[0]), int(case.split()[1]), int(case.split()[2])
    print X, R, C
    '''base case'''
    if X == 1:
        return 'GABRIEL'
    if  R*C < X:
        return 'RICHARD'
    if R*C % X !=0:
        return 'RICHARD'
    
    if X == 2:
        if R*C % 2 == 0:
            return 'GABRIEL'
        
    if X == 3:
        if R <2 or C <2:
            return 'RICHARD'
        else:
            return 'GABRIEL'
    
    if X == 4:
        if R <3 or C <3:
            return 'RICHARD'
        else:
            return 'GABRIEL' 
    return 'RICHARD'

'''for all test cases'''
def run(cases, T):
    answer = []
    for c in cases:
        answer.append(run_each(c))
    return answer

if __name__ == '__main__':
    content = read_input('/Users/yiyang/Desktop/codejam/4/D-small-attempt0.in')
    T = int(content[0])
    cases = content[1:]
    
    answer = run(cases, T)
    write_output('/Users/yiyang/Desktop/codejam/4/output.txt', answer)