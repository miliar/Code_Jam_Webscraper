#!/usr/bin/python2.6
from __future__ import print_function
import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
ans = [ 1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002]
t = input()
for i in range(t):
    a,b = map(int,raw_input().split())
    anse=0
    for j in ans:
        if a<=j*j<=b:anse+=1
    print("Case #{0}: {1}".format(i+1,anse))
