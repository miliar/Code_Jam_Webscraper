#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def calculate(x, r, c):

    if x == 1:
        return "GABRIEL"
        
    if x == 2:
        if r * c % 2 == 0:
            return "GABRIEL"
        else:
            return "RICHARD"
    if x == 3:
        if r*c == 6 or r*c == 9 or r*c == 12:
            return "GABRIEL"
        else:
            return "RICHARD"
    if x == 4:
        if r*c == 12 or r*c == 16:
            return "GABRIEL"
        else:
            return "RICHARD"
'''
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            answer = calculate(x,y,z)
            print "Case #X" + str(x) + "R"+str(y) + "C"+str(z) +  ": " + str(answer)
''' 

'''            
calculate(2,2,2)
calculate(2,1,3)
calculate(4,4,1)
calculate(3,2,3)



4
2 2 2
2 1 3
4 4 1
3 2 3
'''

f = open("D-small-attempt2.in", "r")
#f = open("O.in", "r")
#f = open("C-small-attempt1.in", "r")
#f = open("C-small-attempt0.in", "r")
#f = open("D.in", "r")

T = int(f.readline())

for x in range(0, T):
    readline = f.readline().split(" ")
    X = int(readline[0].strip())
    R = int(readline[1].strip())
    C = int(readline[2].strip())
    answer = calculate(X,R,C)
    print "Case #" + str(x+1) + ": " + str(answer)

'''
varchar = ['1', 'i', 'j', 'k']
for x in varchar:
    for y in varchar:
        result = calculate(x, y)
        if result[0] == 1:
            sign = "+"
        else :
            sign = "-"
        print x +" . " + y + " = " +  sign + result[1]
'''