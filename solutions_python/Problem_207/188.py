import numpy as np
import sys
import itertools


def solve(basic):
    trans=basic
    res=[]
    forb=-1
    imp=0
    priority=-1
    
    while sum(basic)!=0:
            if forb !=-1:
                trans=np.delete(basic,forb)
            if sum(trans)==0 and sum(basic)!=0:
                imp=1
                break
            
            if basic[priority] == max(trans) and priority!= forb:
                    res.append(['R','Y','B'][priority])
                    neg=np.array([0,0,0])
                    neg[priority]=-1
                    basic+=neg
                    forb=priority
                    
            else:        
                for (i,aux) in enumerate(basic):
                    if aux == max(trans) and i!= forb:
                        res.append(['R','Y','B'][i])
                        neg=np.array([0,0,0])
                        neg[i]=-1
                        basic[i]-=1
                        if forb==-1:
                            priority=i
                        forb=i
                        break
            #if case==95:
            #    print basic
            #    print res
        
    if res[0]==res[-1] or imp==1:
        res=['I','M','P','O','S','S','I','B','L','E']
        
    return res



f=open('B-large (1).in', 'r')
f2=open('2_output.ou', 'w')

init=0
case=1
aliii=int(f.readline())


while case <= aliii:
    
    b=f.readline().replace('\n','').split(' ')
    
    R=int(b[1])
    Y=int(b[3])
    B=int(b[5])
    
    O=int(b[2])
    G=int(b[4])
    V=int(b[6])
    
    R_i=R-G
    Y_i=Y-V
    B_i=B-O
    
    
    
    
    if (R_i<=0 and G!=0) or (Y_i<=0 and V!=0) or (B_i<=0 and O!=0):
        res=['I','M','P','O','S','S','I','B','L','E']

    
    else:
        basic=np.array([R_i,Y_i,B_i])
        res=solve(basic)
        
    
    if res[0] != 'I':
  
        for (i,aux) in enumerate(res):
            if aux=='R':
                res.insert(i+1,'GR'*G)
                break
        for (i,aux) in enumerate(res):
            if aux=='Y':
                res.insert(i+1,'VY'*V)
                break
        for (i,aux) in enumerate(res):
            if aux=='B':
                res.insert(i+1,'OB'*O)
                break
        
    if R!=0 and G!=0 and max(Y,B,V,O)==0 and R_i==0:
        res=['RG'*G]
    
    if Y!=0 and V!=0 and max(R,B,G,O)==0 and Y_i==0:
        res=['YV'*V]
    if O!=0 and B!=0 and max(Y,R,V,G)==0 and B_i==0:
        res=['BO'*O]
    
    
    
    
    
    print 'Case #'+str(case)+": "+''.join(res)
    f2.write('Case #'+str(case)+": "+''.join(res)+'\n')
    case+=1