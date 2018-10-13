__author__ = 'sarrtv'

import fileinput

f = fileinput.input()
n_test_cases = int(f[0])
tests=[]
max_S_vec=[]
for line in f:
        ls = line.split()
        max_S= int(ls[0])
        max_S_vec.append(max_S)
        tests.append([int(i) for i in ls[1]])
        assert(len(tests[-1])== max_S+1)

assert(len(tests)==n_test_cases)

def compute_problem(test):
    if len(test)==1:
        return [0]
    cumsum = [sum(test[:i+1]) for i in range(len(test))]
    diff_vector = [i-cumsum[i-1] for i in range(1,len(test))]
    return diff_vector

f = open('results_large.txt', 'w')
for ix, test in enumerate(tests):
    f.write('Case #%i: %i\n' %(ix+1, max(max(compute_problem(test)),0)))
f.close()
