import math

def demo():
    a=open("B-large.in")
    b=a.readlines()
    outf=open("out.txt","w")
    
    for i in range(int(b[0])):
        res=check(b[i+1])        
        print "Case #"+str(i+1)+": "+str(res)
        outf.write("Case #"+str(i+1)+": "+str(res)+"\n")
    outf.close()

C=0
F=0.0
X=0.0

def t(i):
    global C,F
    return C/(2.0+i*F)

def check(row):
    global C,F,X
    C,F,X=row.split()
    C=float(C)
    F=float(F)
    X=float(X)

    N=int(X/C)+1
    
    resarray=[X/2.0]
    res=0.0
    for i in range(N)[1:]:
        res+=t(i-1)
        resarray.append(res+X/(2.0+i*F))
    return min(resarray)

raw_input("Got data?")
demo()

