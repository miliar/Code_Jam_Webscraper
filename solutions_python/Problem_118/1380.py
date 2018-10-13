from math import *

def palindrome(num):
    st=str(num)
    return (st==st[::-1])

fl=open("input.txt","r")
out=open("output.txt","w")
cases=int(fl.readline())
for i in range(0,cases):
    start,end=fl.readline().split()
    start,end=int(start),int(end)
    newst=int(ceil(sqrt(start)))
    newend=int(ceil(sqrt(end)))
    count=0
    print(newst,newend)
    for num in range(newst,newend+1):
        sq=num*num
        if palindrome(num) and palindrome(sq):
            if(sq<=end) and (sq>=start):
                count+=1
    st="Case #"+str(i+1)+": "+str(count)+"\n"
    out.write(st)
fl.close()
out.close()
