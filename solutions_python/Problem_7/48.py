from copy import *
from math import *
import psyco ; 
from psyco.classes import *


f=open("1A-large.in")

#f=open("bound.txt")

def I():
    s=f.readline()
    s=s.strip()
    s=int(s)
    return s

def S():
    s=f.readline()
    s=s.strip();
    return s

def read():
    s=S()
    s=s.split()
    for i in range(len(s)):
        s[i]=int(s[i])
        
    
    n=s[0]
    A=s[1]
    B=s[2]
    C=s[3]
    D=s[4]
    x0=s[5]
    y0=s[6]
    M=s[7]
    matrix =[[0,0,0],[0,0,0],[0,0,0]]
    X = x0; Y = y0
    matrix[X%3][Y%3]+=1
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        matrix[X%3][Y%3]+=1
    return matrix

def calc(mat):
    total = 0
    for i in range(3):
        for j in range(3):
            total += mat[i][j]*(mat[i][j]-1)*(mat[i][j]-2)/6
    for i in range(3):
        total +=mat[i][0]*mat[i][1]*mat[i][2]
    for j in range(3):
        total +=mat[0][j]*mat[1][j]*mat[2][j]
    total +=mat[0][0]*mat[1][1]*mat[2][2]
    total +=mat[0][0]*mat[2][1]*mat[1][2]
    total +=mat[1][0]*mat[0][1]*mat[2][2]
    total +=mat[1][0]*mat[2][1]*mat[0][2]
    total +=mat[2][0]*mat[1][1]*mat[0][2]
    total +=mat[2][0]*mat[0][1]*mat[1][2]
    return total
    


noTests = I()

for t in range(noTests):
    mat=read()
    ans=calc(mat)
    print "Case #%d: %d" %(t+1,ans)
    
    
    
    














