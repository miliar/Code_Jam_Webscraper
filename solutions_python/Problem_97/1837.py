import os
temp=open('C:\Users\DELL\Downloads\C-small-attempt3.IN').read().splitlines()
count=0
cases=int(temp[count])
num=0
count+=1
prnt=[]
while num<cases:
    recycled=0
    a=[]
    stir=temp[count]
##    print stir
    n=0
    for i in stir:
        if i==' ':
            beg=n
            n=0
        else:
            n=n*10+int(i)
    end=int(n)
##    print beg
##    print end
    count+=1
    for z in range(beg,end+1):
        z1=str(z)
##        print "New",z1
        i=1
        x=len(z1)
        c=0
        flag=1
        for t in z1:
            if z1[0]==t:
                c+=1
        if c==x:
            flag=0
##        print "Length",x
        while i<x:
##            print z
            z1=int(z)
            z2=int(z1%(10**i))
            z1=int(z1/(10**i))
            z1=z2*(10**(x-i))+z1
##            print z1,":",z
            if not int(z1)==int(z) and (z1<=end) and (z1>=beg) and flag==1:
##                print z2
##                print z,":",z1
##                print "increment"
                recycled+=1
            i+=1
    prnt.append(recycled/2)
    num+=1
n=0
while n<cases:
    print 'Case #%d:'%(n+1),prnt[n]
    n+=1
