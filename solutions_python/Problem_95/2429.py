import os
conv={'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
temp=open('C:\Users\DELL\Downloads\A-small-attempt2.IN').read().splitlines()
count=0
cases=int(temp[count])
n=0
count+=1
##while count<32:
##    print temp[count]
##    count+=1
prnt=[]
while n<cases:
    out=""
    for i in temp[count]:
        if(not i==' '):
            out=out+conv[i]
        else:
            out=out+i
    count+=1
    prnt.append(out)
    n+=1
n=0
while n<cases:
    print 'Case #%d:'%(n+1),prnt[n]
    n+=1
        
