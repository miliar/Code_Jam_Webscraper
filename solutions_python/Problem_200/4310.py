#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:48:06 2017

@author: bitcurian
"""
import sys

def getDiff(st,index):
    num,i=st,index
    x='10'+'0'*i
    num=num%int(x)
    return num
    
    
    
    
def tidyFunction(n):
    s=str(n)
    digits=len(s)
    for i in range(digits-1,0,-1):
        h=0
        #print(s[i],s[i-1],i,i-1)
        if(s[i]<s[i-1]):
            c=(digits-1)-i
            h=getDiff(n,c)
            h+=1
            
           
            n-=h
            s=str(n)
            
    return n     
        
    
def main():
    '''
    s='12345'
    for i in xrange(len(s)):
        print(getDiff(s,i))
    '''
    F=open("B-large.in",'r')
    F1=open("answersL.txt",'w')
    '''
    test_cases=int(raw_input())
    
    
    a=[]
    for i in xrange(test_cases):
        
        a.append(int(raw_input()))
    '''
    test_cases=int(F.readline())
    
    
    a=[]
    for i in xrange(test_cases):
        
        a.append(int(F.readline()))
    j=1        
    for i in a:
        tidy=tidyFunction(i)
        print F1.write("Case #%d: %d \n"%(j,tidy))
        j+=1   
    
    F.close()
    F1.close()
if __name__=="__main__":
    main()    