# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:16:47 2017

@author: Sebastian
"""

def swap(i,K,line):
    if i + K > len(line):
        print("Wrong arguments")
    line = list(line)
    for j in range(i,i+K):
        if line[j] == '-':
            line[j] = '+'
        elif line[j] == '+':
            line[j] = '-'
    line = ''.join(line)
    return line

def solve(num,line):
    line,K = line.split(" ")
    S = len(line)
    K = int(K)
    swaps = 0
    for i in range(S-K+1):
        if line[i] == '-':
            line = swap(i,K,line)
            swaps = swaps+1
    strToReturn = "Case #"+str(num+1)+": "+str(swaps)
    for i in range(S):
        if line[i] == '-':
            strToReturn = "Case #"+str(num+1)+": IMPOSSIBLE"
            break
    return strToReturn
    
filename = str(input("Filename to open:"))
file = open(filename)
T = int(file.readline())
solveFile = open(filename+"_solved.txt",'w')
for i in range(T):
    erg = solve(i,file.readline())
    print(erg)
    if i != T-1:
        solveFile.write(erg+"\n")
    else:
        solveFile.write(erg)