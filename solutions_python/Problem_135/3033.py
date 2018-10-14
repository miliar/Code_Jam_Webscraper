import sys

problem = 'a-small'

testcase = open(problem + '.in','r')
solution = open(problem + '.out','w')
cache_stdin, sys.stdin = sys.stdin, testcase

def row():
    row = int(input()) - 1
    line = None
    for i in range(4):
        scan = input().split()
        if i == row:
            line = {int(i) for i in scan}
    return line
    
t = int(input())
for i in range(t):
    guess = row() & row()
    if len(guess) == 1:
        s = '%s' %(list(guess)[0],)
    elif len(guess)==0:
        s = 'Volunteer cheated!'
    else:
        s = 'Bad magician!'
        
    print('Case #' + str(i+1) + ': ' + s, file=solution)

    
solution.close()
testcase.close()
sys.stdin = cache_stdin
