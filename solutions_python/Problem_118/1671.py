#!/usr/bin/env python
#coding: utf-8

__author__ = "Pedro Pérez Sánchez <pedropobla@gmail.com>"

import sys
import math

def isPalindrome(w):
    return w == w[::-1]

def nextPalindrome(num):
    length=len(str(num))
    oddDigits=(length%2!=0)
    leftHalf=getLeftHalf(num)
    middle=getMiddle(num)
    if oddDigits:
        increment=pow(10, length/2)
        newNum=int(leftHalf+middle+leftHalf[::-1])
    else:
        increment=int(1.1*pow(10, length/2))
        newNum=int(leftHalf+leftHalf[::-1])
    if newNum>num:
        return newNum
    if middle!='9':
        return newNum+increment
    else:
        return nextPalindrome(roundUp(num))
 
def getLeftHalf(num):
    return str(num)[:len(str(num))/2]
 
def getMiddle(num):
    return str(num)[(len(str(num))-1)/2]
 
def roundUp(num):
    length=len(str(num))
    increment=pow(10,((length/2)+1))
    return ((num/increment)+1)*increment

if __name__ == '__main__':
    T = int( sys.stdin.readline() )
    for t in range(T):
        result = 0
        [A,B] = [int(x) for x in sys.stdin.readline().split()]
        A = int(math.ceil( math.sqrt(A)))
        B = int(math.floor( math.sqrt(B)))
        x = nextPalindrome(A-1)
        while(x<=B):
            if( isPalindrome(str(x*x)) ): result+=1
            x = nextPalindrome(x)

        print "Case #"+ str(t+1) +": "+ str(result)
    exit(0)