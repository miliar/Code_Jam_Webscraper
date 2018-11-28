#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open('A-large.in','r')
g = open('A-large.ou','w')

def solution(string, K):
    turns = 0
    for k in range(len(string)-K+1):
        if string[k] == '-':
            firstK = string[k:k+K]
            firstK = firstK.replace('-','?')
            firstK = firstK.replace('+','-')
            firstK = firstK.replace('?','+')
            string = string[:k]+ firstK + string[k+K:]
            turns += 1
    if string.count('-') != 0:
        return 'IMPOSSIBLE'
    else:
        return str(turns)


n = int(f.readline()[:-1])
for k in range(n):
    line = f.readline()[:-1].split(' ')
    string = line[0]
    K = int(line[1])
    g.write('Case #'+str(k+1)+': '+solution(string, K)+'\n')



f.close()
g.close()