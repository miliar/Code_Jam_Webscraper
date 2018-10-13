#!/usr/bin/env python

def intersect(rope1, rope2):
    (h11, h12) = rope1
    (h21, h22) = rope2
    if ((h11-h21) * (h12-h22) < 0):
        return True
    else:
        return False
    
def read_case(read):
    [P] = read_int_line(read)
    M = read_int_line(read)
    C = []
    for x in xrange(P):
        C.append(read_int_line(read))    
    return P, M, C

def solve_case(data):
    P, M, C = data
    INF = 10000000
    R = [0]*len(M) + [[INF]*(P-x) + [0] + [INF]*x for x in M]
    matches = len(M)/2
    current = matches-1
    level = 0
    for x in xrange(len(M)-1, 0, -1):
        
        R[x] = [min(min(R[x*2][:i+1]) + min(R[x*2+1][:i+1]),
                    min(R[x*2][:i+2]) + min(R[x*2+1][:i+2]) + C[level][current]
                   )
                for i in xrange(P+1)] + [INF]
        #print R[x]
                
        current -= 1
        if (current < 0):
            matches /= 2
            current = matches-1
            level += 1
        
    return R[1][0]
    

def main():
    solve_n_cases(solve_case, read_case)

##### PROBLEM VARIABLES ######

INFILENAME = 'B-large.in'
OUTFILENAME = 'output.out'

##### PROBLEM TEMPLATE ######

from time import time
from multiprocessing import Pool
   
def init_io():
    read = open(INFILENAME, 'rt')
    write = open(OUTFILENAME, 'wt')
    return (read, write)

def deinit_io(read, write):
    read.close()
    write.close()
    
def read_token_line(read, tokenparsefunction):
    return [tokenparsefunction(x)
                for x in read.readline().split()]
    
def read_int_line(read):
    return read_token_line(read, int)
    
def output_case_sharp(write, casenum, result):
    write.write( 'Case #{0}: {1}\n'.format(casenum, result) )

def solve_n_cases(solve_function, read_function, output_function = output_case_sharp):
    read, write = init_io()
    
    cases_num = int(read.readline())
    current_case = 1
    cases_data = []
    #p = Pool()
    
    started = time()
    
    while (cases_num>0):
        cases_data.append( read_function(read) )        
        cases_num -= 1
        
    results = map(solve_function, cases_data)
    
    for result in results:
        output_function(write, current_case, result)
        current_case += 1
        
    finished = time()
    
    print 'Finished in {0:.2} sec.'.format(finished-started)
    
    deinit_io(read, write)

if __name__ == "__main__":
    main()