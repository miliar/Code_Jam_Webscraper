from math import *

def stall(N, k):
    N = int(N)
    k = int(k)
    L = floor(log(k, 2)) + 1
    num_split = ceil((N - (k - 1))/ (2**(L-1)))
    
    min_ = floor((num_split - 1)/2)
    max_ = ceil((num_split - 1)/2)
    
    return max_, min_

f_r = open('C-small-2-attempt0.in', 'r')
f_w = open('answer.out', 'w')

t = f_r.readline()

problems = [list(x.split(' ')) for x in f_r]

for index, x in enumerate(problems):
    max_, min_ = stall(*x)
    
    f_w.write('Case #' + str(index+1) + ': ' + str(max_) + ' ' + str(min_) + '\n')
    
f_w.close()

