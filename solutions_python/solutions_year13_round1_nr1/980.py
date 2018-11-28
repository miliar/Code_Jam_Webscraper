# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 09:03:39 2013

@author: jlb
"""

from math import *

def forward(r,t,n):
    num=t-(2*r-1)*(n)-2*(n)**2
    return num
    
def solve(r,t):
#    root=(sqrt((r+2)**2+4*(r+1)*t)-(r+2))/(2*(r+1))
    root=(sqrt((-1+2*r)**2+8*t)-(2*r-1))/4
    root=floor(root)-1
    for i in range(5):
        root=root+1
#        print(r,t,root, forward(r,t,root))
        if forward(r,t,root)<0:
            break    
    return root-1



def Atest(inP,outP):
    with open(inP) as inFile:
        with open(outP,'w') as outFile:
            num=int(inFile.readline())
            print(num)
            for i in range(num):
                line=inFile.readline()
                rStr,tStr=line.split(r" ")
                r=long(rStr)
                t=long(tStr)
                print(r,t)                
                max_ring=long(solve(r,t))
                print(max_ring)
                outFile.write("Case #{0}: {1}\n".format(i+1,max_ring))

def main():
    inputF=r"/home/jlb/Project/CFamily/CodeBuf/A-small-attempt1.in"
    outputF=r"/home/jlb/Project/CFamily/CodeBuf/out1.txt"
    Atest(inputF,outputF)
#    r=10000000000000000L
#    t=1000000000000000000L
#    num=forward(r,t,49)
#    print(forward(r,t,50))

    
    
if __name__=="__main__":
    main()

    
