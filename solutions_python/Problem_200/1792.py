# -*- coding: utf-8 -*-
import fractions
import math

def printResult(i,result,outfile):
    print('Case #' + str(i + 1) + ': ' + result)
    outfile.write('Case #' + str(i + 1) + ': ' + result + '\n')

fileName = 'B-large'
with open(fileName+'.in', 'r') as infile, open(fileName + '_output.out', 'w') as outfile:
   
    T = int(infile.readline().split('\n')[0]);
    
    for z in range(0,T):

        line = infile.readline().split('\n')[0].split(' ');
        nums = list(line[0])
        nums.reverse()
        N = len(nums)
        for i in range(0,N-1) :
            if nums[i+1] > nums[i] :
                nums[i+1] = str(int(nums[i+1])-1)
                for k in range(0,i+1) :
                    nums[k] = '9'

        nums.reverse()
        result = str(int(''.join(nums)))
        printResult(z, result, outfile);



        
    
    
    
