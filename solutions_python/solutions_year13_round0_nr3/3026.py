#!/usr/bin/python
import math
def sqr_num(little,big):
    sqr=0
    for i in range(little,big):
        if i*i<=big:
            sqr=i
    return sqr

def if_loopback(number):
    if int(number) < 10:
        return 0
    number=str(number)
    for i in range(0,int(len(number)/2)):
        if number[i]!=number[len(number)-i-1]:
            return 1
    return 0
def  if_int(number):
    if number*100000%100000==0:
        return 0
    return 1


file=open("C-small-attempt5.in","r")
flag=0
num=1
logfile=open("log","a")
for lines in file:
    if flag==0:
        flag=int(lines)
        continue
    d=0
    rangelist=lines.split()
    little=int(rangelist[0])
    big=int(rangelist[1])
    for i in range(little,big+1):
        c=math.sqrt(i)
        if if_int(c)==0:
            c=math.trunc(c) 
            if if_loopback(i)==0 and if_loopback(c)==0 :
                d=d+1
    print ("Case #%d: %d" %(num,d),file=logfile)
    num=num+1
logfile.close()
