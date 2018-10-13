#!/usr/bin/python
# coding: utf-8
from sys import stdin, stdout

t=int(raw_input())
list=stdin.readlines()
t=0
for i in list:
    t+=1
    (max,arr)=i.split(' ')
    max=int(max)+1
    cnt=0
    tot=0
    for j in xrange(max):
        tmp=0
        if(j>tot):
            tmp=j-tot
            cnt+=tmp
        tot+=int(arr[j])+tmp
    stdout.write(str("Case #"+str(t)+": "+str(cnt))+"\n")