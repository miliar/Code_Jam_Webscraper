#! /usr/bin/python
import sys
    
def main():
    file1=open(sys.argv[1])
    a=file1.readlines()
    cases=int(a.pop(0))
    values=[]
    for x in range(cases):
        values.append(findyears(a[x].split()))
    strings=[]
    for x in range(cases):
        string1="Case #"+str(x+1)
        string1+=": "+str(values[x])        
        strings.append(string1)
    f=open("Output.txt","w")
    for x in strings:
        f.write(x+"\n")
    
    
def findyears(list1):
    numcases=int(list1.pop(0))
    for x in range(numcases):
        list1[x]=int(list1[x])
    minval=min(list1)
    for x in range(numcases):
        list1[x]-=minval
    gcd=gcdlist(list1)
    if 0==minval%gcd:
        return 0
    return gcd-(minval%gcd)



    
def gcdlist(list1):
    current=gcd(list1[0],list1[1])
    index=2
    while index<len(list1):
        current=gcd(current,list1[index])
        index+=1
    return current
    

def gcd(a,b):
    while b<>0:
        t=b
        b=a%b
        a=t
    return a

if __name__ == "__main__":
    main()


