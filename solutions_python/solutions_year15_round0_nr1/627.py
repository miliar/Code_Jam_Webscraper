#! /opt/local/bin/python

#f = open("A-small-attempt1.in")
f = open("A-large.in")
#f = open("exA.in")

T= int(f.readline().strip());

for t in range(T):
    (Smax,Ni)=  f.readline().strip().split();
    Smax=int(Smax)
    Addi,cumsum=0,int(Ni[0])
    for i in range(1,Smax+1):
        #print cumsum,i,Addi
        if(cumsum<i):
            Addi+= i-cumsum
            cumsum+=i-cumsum
        cumsum += int(Ni[i])

    print "Case #"+str(t+1)+": "+str(Addi)
