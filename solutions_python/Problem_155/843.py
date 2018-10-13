
import sys
lines = map(lambda line:line.strip(),sys.stdin.readlines())
n = int(lines[0])
problem_cases = map(lambda line:line.split(), lines[1:])
assert n == len(problem_cases)

def prob_solver(*prob_args):
    max_s = int(prob_args[0])
    list_s = map(int,prob_args[1])
    assert max_s + 1 == len(list_s)
    add_n = 0 
    clapping_n = list_s[0]
    for j in range(1,max_s+1):
        while clapping_n < j:
            clapping_n = clapping_n + 1 
            add_n = add_n + 1 
        
        clapping_n = clapping_n + list_s[j] 
        
    return add_n

for case_i in range(n):
    #print problem_cases[case_i]
    print "Case #{case_i}: {solution}".format(case_i=case_i+1,
                                              solution=prob_solver(*problem_cases[case_i]))
    
