
import numpy as np
#from numpy import *
import sys
lines = map(lambda line:line.strip(),sys.stdin.readlines())
n = int(lines[0])
problem_cases = map(lambda line:line.split(), lines[1:])
assert n == len(problem_cases)

test_prob_sol = [0,1,2,0] 

for case_i in range(n):
    max_s = int(problem_cases[case_i][0])
#     print problem_cases[case_i][1]
    s=problem_cases[case_i][1]
    s=np.array(map(int,list(s)))
    l=len(s)
    c=0
    if l!=0 and s[0]==0:
        c+=1
        s[0]=c
    if l!=0:    
        for i in range(l):
            p=sum(s[x] for x in range(i))
            if p<i:
                s[0]+=(i-p)
                c+=(i-p)
    print "Case #{case_i}: {solution}".format(case_i=case_i+1,solution=c) 