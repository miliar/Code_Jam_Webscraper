
PROBLEM_LENGTH = 2

import sys
lines = map(lambda line:line.strip(),sys.stdin.readlines())
n = int(lines[0])
problem_cases = map(lambda line:line.split(), lines[1:])
assert n*PROBLEM_LENGTH == len(problem_cases)

import numpy as np

class Mem(object):
    def __init__(self):
        self.res = {}

    def __call__(self, f):
        
        def new_f(Pis):
            Pis = np.sort(Pis)
            Pis_key = ",".join(map(str,Pis))
            
            if not (Pis_key in self.res):
                self.res[Pis_key] = f(Pis)
            
            return self.res[Pis_key]
        
        return new_f
            
            
mem = Mem()
        
@mem
def g(Pis):
    #print "~~~~~~~~~~~~~~~~~~~"
    Pis = np.sort(Pis)
    
    if all(Pis <= 0):
        return 0
    elif all(Pis == 1):
        return 1
    
    else:
        eaten_array = Pis - 1
        eaten_array = np.sort(eaten_array[eaten_array > 0])
        #print "eaten_array = ",eaten_array
        
        all_results = [g(eaten_array)+1]
        
        for k in range(1,Pis[-1]):
            
            separation_list = Pis[:-1].tolist()
            separation_list.extend([Pis[-1] - k,k])
            separation_array = np.sort(np.array(separation_list))
            
            all_results.append(g(separation_array)+1)
        
        return min(all_results)
        
    
    
    
def prob_solver(*prob_args):
    n_plates = int(prob_args[0][0])
    Pis = np.array(map(int, prob_args[1]))
    
    return g(Pis)


for case_i in range(n):
    print "Case #{case_i}: {solution}".format(case_i=case_i+1,
                                              solution=prob_solver(*problem_cases[PROBLEM_LENGTH*case_i:PROBLEM_LENGTH*case_i+PROBLEM_LENGTH]))