#!/usr/bin/python
# -*- coding: utf8 -*-

import sys

def chbase(n,base):
    result=0
    for i,ch in enumerate(reversed(n)):
        result+=int(ch)*base**i
    return result

f=open("A-small.in")
o=open("A-small.out","w")

N=int(f.readline().rstrip("\n"))
#input=f.readlines()
#s=input.pop(0)

for i,line in enumerate(f):
    line=line.rstrip("\n")
    print line
    table={}
    numbers=""
    nextno=2
    for ch in line:
        if ch in table:
            numbers=numbers+table[ch]
        else:
            if table=={}:
                table[ch]="1"
                numbers=numbers+"1"
                continue
            if ch not in table:
                if len(table)==1:
                    table[ch]="0"
                    numbers=numbers+"0"
                else:
                    table[ch]=str(nextno)
                    numbers=numbers+str(nextno)
                    nextno+=1
            else:
                numbers=numbers+table[ch]
    print table
    print numbers
    base=len(table)
    if base==1: base+=1
    result=chbase(numbers,base)
    print result
    o.write("Case #"+str(i+1)+": "+str(result)+"\n")
    if i==N-1:break

f.close()
o.close()
        

