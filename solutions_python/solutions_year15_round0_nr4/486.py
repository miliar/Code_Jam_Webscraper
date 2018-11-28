# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:22:52 2015

@author: petrs
"""

f = open('C:\Users\petrs\Downloads\D-small-attempt0.in', 'r')
g = open('C:\Users\petrs\Downloads\soutput4.txt', 'w')

T = int(f.readline().split()[0])

for i in range(T):
    X,R,C = [int(x) for x in f.readline().split()]

    assert X<=4
    
    if R*C % X != 0:
        g.write("Case #%i: RICHARD\n" % (i+1))
    else:    
        if X == 1:
            g.write("Case #%i: GABRIEL\n" % (i+1))
        if X == 2:
            g.write("Case #%i: GABRIEL\n" % (i+1))
        if X == 3:
            if R==1 or C==1:
                g.write("Case #%i: RICHARD\n" % (i+1))
            else:
                g.write("Case #%i: GABRIEL\n" % (i+1))
        if X == 4:
            if R<=2 or C<=2:
                g.write("Case #%i: RICHARD\n" % (i+1))
            else:
                g.write("Case #%i: GABRIEL\n" % (i+1))    


f.close()
g.close()