# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:30:21 2013

@author: learningoutcomes
"""
import re, sys

def tik(sample):
    transpose = []
    for i in zip(*sample):
        transpose.append(''.join(i))
    return transpose
    
def winner(t):
    transpose = []
    for i in zip(*t):
        transpose.append(''.join(t))
    dots = 0
    for i in t:
        num_of_x = len(re.findall(r'X', i))
        num_of_t = len(re.findall(r'T', i))
        num_of_o = len(re.findall(r'O', i))
        num_of_dot = len(re.findall(r'\.', i))
        if num_of_dot:
            dots += 1
        
        if num_of_x == 3 and num_of_t == 1 or num_of_x == 4:
            return 'X won'
        elif num_of_o == 3 and num_of_t ==1 or num_of_o == 4:
            return 'O won'
    count_x = 0
    for i in range(len(t)):
        if t[i][i] == 'X' or t[i][i] == 'T':
            count_x += 1
    if count_x == 4:
        return 'X won'
    count_x = 0
    for i in range(len(t)):
        if t[i][(len(t)-1)-i] == 'X' or t[i][(len(t)-1)-i] == 'T':
            count_x += 1
    if count_x == 4:
        return 'X won'
    count_o = 0
    for i in range(len(t)):
        if t[i][i] == 'O' or t[i][i] == 'T':
            count_o += 1
    if count_o == 4:
        return 'O won'
    count_o = 0
    for i in range(len(t)):
        if t[i][(len(t)-1)-i] == 'O' or t[i][(len(t)-1)-i] == 'T':
            count_o += 1
    if count_o == 4:
        return 'O won'
    
    if dots > 0:
        return 'Game has not completed'
    return 'Draw'
f = []

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as p:
        for i in p.xreadlines():
            f.append(i.strip('\n\r'))
        
        
        input = []
        new = []
        for i in f[1:]:
            if i == '':
                input.append(new)
                new = []
            else:
                new.append(i)
    
    output = open('output.txt', 'w')
    
    for i in range(len(input)):
        p = winner(input[i])
        if p == 'Game has not completed' or p == 'Draw':
            output.write('Case #%d: %s\n' %(i+1, winner(tik(input[i]))))
        else:
            output.write('Case #%d: %s\n' %(i+1, p))