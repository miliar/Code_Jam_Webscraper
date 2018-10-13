
from collections import *
from copy import *
from math import *
from fractions import *
import sys

if __name__=='__main__':
    input=open('A-large.in.txt','r+')
    output=open('A-large.out.txt','w+')

    numCases = int(input.readline().strip())
    for case in range(1,numCases+1):
        [r,c]=input.readline().strip().split()
        r=int(r)
        c=int(c)

        arrows = []
        for i in range(r):
            arrows.append(input.readline().strip())

        should=[]
        for i in range(r):
            should.append([])
            for j in range(c):
                should[i].append('')
        for i in range(r):
            for j in range(c):
                if arrows[i][j]!='.':
                    should[i][j]=should[i][j]+'<'
                    break
            for j in range(c-1,-1,-1):
                if arrows[i][j]!='.':
                    should[i][j]=should[i][j]+'>'
                    break
        for j in range(c):
            for i in range(r):
                if arrows[i][j]!='.':
                    should[i][j]=should[i][j]+'^'
                    break
            for i in range(r-1,-1,-1):
                if arrows[i][j]!='.':
                    should[i][j]=should[i][j]+'v'
                    break
        s=0
        possible = True
        for i in range(r):
            for j in range(c):
                if len(should[i][j])==4:
                    possible = False
        if possible:
            for i in range(r):
                for j in range(c):
                    if (should[i][j]!='') and arrows[i][j] in should[i][j]:
                        s+=1
            output.write("Case #%d: %d\n"%(case,s))
                    
        else:
            output.write("Case #%d: %s\n"%(case,'IMPOSSIBLE'))
        

    input.close()
    output.close()