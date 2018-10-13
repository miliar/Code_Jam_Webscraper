#! /usr/bin/env/python
f1=open("1b.in","r")
f2=open("1b.out","w")
list=(f1.read()).split("\n")
n=long(list[0])
del list[0]
i=long(0)
flag=1
while i<n:
    line=(list[i]).split(" ")
    c=float(line[0])
    f=float(line[1])
    x=float(line[2])
    sum=2.0
    time=0.0
    i=i+1
    while 1:
        if (time+(c/(sum)+(x/(sum+f))))>(time+(x/sum)):
            time=time + (x/sum)
            s="Case #"+str(i)+": "+str(time)+"\n"
            f2.write(s)
            break
        elif c/sum < x/sum:
            time=time + (c/sum)
            sum=sum+f         
f1.close()
f2.close()
    
   
