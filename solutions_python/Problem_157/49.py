#!/usr/bin/python
T = int(raw_input())

i=2;
j=3;
k=4;

multiply_tab = [];
multiply_tab.append([1,i,j,k]);
multiply_tab.append([i,-1,k,-1*j]);
multiply_tab.append([j,-1*k,-1,i]);
multiply_tab.append([k,j,-1*i,-1]) ;

def multiply(x,y):
    if(x<0):
        return -1*multiply_tab[-x-1][y-1]
    return(multiply_tab[x-1][y-1])


for t in xrange(T):
    l=raw_input().split(" ")
    L=int(l[0])
    X=int(l[1])
    acc=1
    acc_i=1
    i_seen=False
    j_seen=False
    acctot=1
    m=raw_input()
    for nn in xrange(min(8,X) ):
        for char in xrange(L):
            ch=m[char]
            cha = 0
            if(ch=='i'):
                cha=i
            if(ch=='j'):
                cha=j
            if(ch=='k'):
                cha=k
            acc=multiply(acc,cha)
            if(i_seen):
                acc_i=multiply(acc_i,cha)
            if(i_seen and acc_i==j):
                j_seen=True
            if(acc==i):
                i_seen=True
        if(nn==0):
            acctot=acc
    sol=True
    
    if((acctot==-1 and (X % 2)==0)
    or (acctot==1) 
    or (acctot!=1 and acctot!=-1 and (X%4)!=2)
    or not i_seen or not j_seen):
        sol = "NO"
    else:
        sol="YES"
    print "".join("Case #"+str(t+1)+": "+sol)

