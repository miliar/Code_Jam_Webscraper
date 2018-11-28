#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 09:12:16 2017

@author: shoom
"""

def remove_leading_zeros(s):
    for i in range(len(s)):
        if int(s[i]) > 0:
            break
    return s[i:]
    

t = int(raw_input())

for test_num in range(1,t+1):
    #read test case
    number = raw_input()
#    print number
    number = remove_leading_zeros(number)
    
    #Solve the problem
    n = len(number)
    if n == 1:
        solution = number
    else:
        digits = [int(number[i]) for i in range(len(number))]
        #find the first case when the number is greater than the next one
        max_num = -1
        for i in range(n-1):
            if digits[i] > digits[i+1]:
                max_num = i
                break
 #       print 'max_num={}; n={}'.format(max_num,n)
        if max_num == -1:
            solution = number  #not found - all ordered
        else:
            #treat the case of 123888881. Find the first 8
            min_num = 0
            for j in range(max_num, 0, -1):
                if digits[j] > digits[j-1]:
                    min_num = j
                    break
  #          print min_num, max_num
            digits[min_num] = digits[min_num]-1
            for i in range(min_num+1,n):
                digits[i] = 9
            solution = ''.join([str(digits[i]) for i in range(n)])
            solution = remove_leading_zeros(solution)
    print "Case #{}: {}".format(test_num, solution)
    
