from copy import *
from math import *

fi=open("L.in")

#f=open("bound.txt")

def I():
    s=fi.readline()
    s=s.strip()
    s=int(s)
    return s

def S():
    s=fi.readline()
    s=s.strip();
    return s

def read(m):
    interior=[]
    value=[]
    value.append(-1)
    interior.append(-1)  #intial value

    for i in range((m-1)/2):
        s=S()
        s=s.split()
        for i in [0,1]:
            s[i]=int(s[i])
        interior.append(s)
        value.append(-1)
    for i in range((m+1)/2):
        value.append(I())
    for i in range((m-1)/2,0,-1):
        if interior[i][0] == 1 :
            value[i]= value[2*i+1]*value[2*i]
        else :
            value[i]= value[2*i+1] or value[2*i]
            
    return [interior,value]    

def f(i,xval,T,m):
    if xval ==  T[1][i] :
        return 0
    else :
        if i> (m-1)/2 :
            return m+1
        else :
            if T[0][i][0] == 1 and T[1][i]==0 :
                lch=T[1][2*i]
                rch=T[1][2*i+1]
                if (T[0][i][1]==1):
                    
                    if (lch or rch):
                        return 1
                    else  :
                        return 1 + min(f(2*i,1,T,m),f(2*i+1,1,T,m))
                else :
                    return f(2*i,1,T,m)+f(2*i+1,1,T,m)
            elif T[0][i][0] == 1 and T[1][i]==1 :
                return min(f(2*i,0,T,m),f(2*i+1,0,T,m))
            elif T[0][i][0] == 0 and T[1][i]==1 :
                lch=T[1][2*i]
                rch=T[1][2*i+1]
                if (T[0][i][1]==1):
                    
                    if not (lch and rch):
                        return 1
                    else  :
                        return 1 + min(f(2*i,0,T,m),f(2*i+1,0,T,m))
                else :
                    return f(2*i,0,T,m)+f(2*i+1,0,T,m)
            else :
                return min(f(2*i,1,T,m),f(2*i+1,1,T,m))
                
    
    


noTest=I()

for t in range(noTest):
    s=S()
    s=s.split()
    M=int(s[0])
    V=int(s[1])
        
    
    T=read(M)
    res=f(1,V,T,M)
    if res > M :
        print "Case #%d: IMPOSSIBLE" %(t+1)
    else   :
        print "Case #%d: %d" %(t+1,res)        
    







