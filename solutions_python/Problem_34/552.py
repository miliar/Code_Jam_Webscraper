'''
Created on Sep 2, 2009

@author: Penn
'''
import re

file=open("A-large.in")

input=file.readline()
temp=input.split(' ')
L=temp[0]
D=temp[1]
N=temp[2]
dict=[]
test=[]

for n in range(0,int(D)):
    dict.append(file.readline())

for n in range(0,int(N)):
    input=file.readline()
    j = 0
    for m in dict:
        if( re.match(input.replace('(', '[').replace(')', ']'), m) != None):
            j += 1
    test.append(j)

output=open("output.out", "w")

for n in range(0,int(N)):
     output.write("Case #%s: %s\n"%(n+1, test[n]))