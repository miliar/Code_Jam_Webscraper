import math

def demo():
    a=open("B-small-1.in")
    b=a.readlines()
    outf=open("out.txt","w")
    
    for i in range(int(b[0])):
        res=check(b[i+1])        
        print "Case #"+str(i+1)+": "+str(res)
        outf.write("Case #"+str(i+1)+": "+str(res)+"\n")
    outf.close()

def check(r):
    r1=r.split()
    for i in range(len(r1)):
        r1[i]=int(r1[i])
    A=r1[0]
    B=r1[1]
    K=r1[2]
    
    counter=0
    
    k=range(K)
    
    for i in range(A):
        for j in range(B):
            if i&j in k:
                counter+=1
    return counter

raw_input("Got data?")
demo()
