
import sys
lines = map(lambda line:line.strip(), sys.stdin.readlines())
n = int(lines[0])
problem_cases = map(lambda line:line.split(), lines[1:])
assert n == len(problem_cases)

if n==4:
    test_prob_sol = [0,1,2,0]
else:
    test_prob_sol = [0,1,2,0, 4]

for case_i in range(n):
    max_s = int(problem_cases[case_i][0])
    string = problem_cases[case_i][1]
    
    cumulated_aud = 0
    solution= 0
    if max_s==0:
        solution= 0
    else:
        for d in range(len(string)):
            if cumulated_aud>= d:
                cumulated_aud += int(string[d])
            else:
                solution += d - cumulated_aud
                cumulated_aud = d + int(string[d])
    
    #print "Case #{0}: {1} {2} {3}".format(case_i, test_prob_sol[case_i] , solution, test_prob_sol[case_i] ==solution)
    print "Case #{0}: {1}".format(case_i+1, solution )