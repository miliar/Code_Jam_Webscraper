# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 22:57:50 2017

@author: Bredock
"""

file = "G:\Programming\Google Jam\A-large.in"
file_out = "G:\Programming\Google Jam\A-small-attempt0.out"
f = open(file)
g = open(file_out, "w")
f.readline()



def findNeg(text):
    return text.find("-")

def flip(pan):
    if (pan == '-'):
        return '+'
    else:
        return '-'

def flipPancackes(text, index, flipper):
    for i in range(0, flipper):
        indice = index + i
        text = text[:indice] + flip(text[indice]) + text[indice+1:]
    return text

line = f.readlines()
num_case = 0
for l in line:
    num_case += 1
    pancackes, flipper = l.split()
    cambios = 0
    done = False
    while (not done):
        neg = findNeg(pancackes)
        if (neg < 0):
            done = True
        else:
            if (len(pancackes) < (int(neg) + int(flipper))):
                done = True
                cambios = "IMPOSSIBLE"
            else:
                pancackes = flipPancackes(pancackes, neg, int(flipper))
                cambios += 1
    g.write("Case #"+str(num_case)+": "+str(cambios)+"\n")
g.close()