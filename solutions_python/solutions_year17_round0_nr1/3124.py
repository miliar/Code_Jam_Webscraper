#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:41:57 2017
Oversized Pancake Flipper
"""
import sys, re, math

def solution(line):
    input = line.split()
    K = int(input[1])
    inputlist = list(input[0])
    totallen = len(inputlist)
    count = 0
    pointer = 0

    while (pointer < totallen-K):
        sign = inputlist[pointer]
        if sign == '+':
            pointer += 1
        else:
            i = pointer
            while (i >= pointer and i < pointer +K):             
                if inputlist[i] == '-':
                    inputlist[i] = '+'
                else:
                    inputlist[i] = '-'
                i +=1                           
            count += 1
          
        
    while pointer < totallen-1:
        if inputlist[pointer] == inputlist[pointer +1]:
            pointer += 1
        else:
            break
        
    if (pointer == totallen-1 and inputlist[totallen -1] == '-'):
        return count+1
    elif (pointer == totallen-1 and inputlist[totallen -1] == '+'):
        return count
    else:
        return "IMPOSSIBLE"
        
            
sys.stdin = open("A-large.txt", "r")
sys.stdout = open("A-large-out.txt", "w")
T = int(sys.stdin.readline())
t = 0
while True:
    line = sys.stdin.readline().rstrip()
    if not line:
        sys.exit(1)
    print 'Case #%d: %s' % (t + 1, solution(line))
    t += 1