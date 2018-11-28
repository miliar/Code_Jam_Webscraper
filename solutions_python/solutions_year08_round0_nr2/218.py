f = open("B-large.in")
def integer():
    s=f.readline()
    s=s.strip()
    s=int(s)
    return s

def string():
    s=f.readline()
    s=s.strip()
    return s

def splitspace():
    s=f.readline()
    s=s.strip()
    s=s.split()
    return s
Blist={}
Alist={}

class train():
    def __init__(self, tim, sta):
                self.status = sta
                self.time = tim
                
    def __cmp__(tr1, tr2):
       if tr1.time < tr2.time: return -1
       if tr1.time > tr2.time: return 1
       if tr1.status == "A": return -1
       else: return 1

def adder(strng,d,t,S):
    s=strng.split(":")
    Time=int(s[0])*60+int(s[1])+t
    l=train(Time,S)
    d.append(l)
    
def calculate(d):
    arr=0
    notrains=0
    for x in d:
        if x.status=="D":
            if arr > 0 :
                arr=arr-1
            else :
                notrains =notrains + 1
        if x.status=="A":
            arr = arr + 1
    return notrains

notest=integer()

for i in range(notest):
    Blist=[]
    Alist=[]
    T=integer()
    temp=splitspace()
    A=int(temp[0])
    B=int(temp[1])
    
    for p1 in range(A):
        temp=splitspace()
        adder(temp[0],Alist,0,"D")
        adder(temp[1],Blist,T,"A")

    for p2 in range(B):
        temp=splitspace()
        adder(temp[0],Blist,0,"D")
        adder(temp[1],Alist,T,"A")
    Alist.sort()
    Blist.sort()
    tA=calculate(Alist)
    tB=calculate(Blist)
    
    #print Alist
    #print Blist
    print "Case #%d: %d %d" %(i+1,tA,tB)
    
    
