# -*- coding:utf-8 -*-

import os
import sys
import array
import math
import pdb
import re

current_path = os.path.dirname(os.path.abspath(__file__))

input_file = open(os.path.join(current_path,'input.in'))
input = input_file.read().split('\n')
input_file.close()


T = int(input[0])
input = input[1:]
input_data=[]

class dataClass:
    def __init__(self, N, name):
        self.N = N
        self.name = name
    def fact(x):
        return x*fact(x-1)
    def comb(m,n):
        if m == n:
            return 1
        else:
            return m*comb(m-1,n)
    def combination(m,n):
        return comb(m,n)/fact(n)
    
def solve(data):
    pat = re.compile(r'([^aeiou]{%d})'%(data.N))
    pat2 = re.compile('[aeiou]')
    iterator = pat.finditer(data.name)
    N_value=0
    N_seq = []
    
    for mat in iterator:
        try:
            endpoint = pat2.search(data.name[mat.end():]).start()+mat.end()
        except:
            endpoint = len(data.name)+1
        try:
            max_p = 0
            for mat2 in pat2.finditer(data.name[:mat.start()+1]):
                if mat2.end()>max_p:
                    max_p = mat2.end()
            startpoint=max_p
        except:
            startpoint = 0
        #pdb.set_trace()
        for start_pos in range(0,endpoint-data.N+1):
            for end_pos in range(startpoint+data.N,len(data.name)+1):
                if end_pos-start_pos >= data.N and not (start_pos, end_pos) in N_seq:
                    N_seq += [(start_pos,end_pos)]
    return len(N_seq)


for case in range(T):
    input_data += [dataClass(int(input[0].split(' ')[1]),input[0].split(' ')[0])]
    input = input[1:]

#pool=Pool(processes=4)
result = map(solve,input_data)




output_file = open(os.path.join(current_path,'output.txt'),'w')
for i in range(T):
    output_file.write('Case #%d: %d\n'%(i+1,result[i]))

output_file.close()
