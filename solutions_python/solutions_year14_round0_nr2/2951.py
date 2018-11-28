import sys

problem = 'b-small'

testcase = open(problem + '.in','r')
solution = open(problem + '.out','w')
cache_stdin, sys.stdin = sys.stdin, testcase

def cookie(C,F,X):
    c = 2.
    t = 0.
    while C*(c+F) < F*X :
        t += C/c
        c += F
        
    t += X/c
    return "%.7f" % (t,)

t = int(input())
for i in range(t):
    C,F,X = [float(j) for j in input().split()]
    print('Case #' + str(i+1) + ': ' + cookie(C,F,X), file=solution)

    
solution.close()
testcase.close()
sys.stdin = cache_stdin
