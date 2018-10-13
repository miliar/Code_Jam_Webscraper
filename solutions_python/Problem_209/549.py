import numpy as np
import sys
import itertools

f=open('A-large (1).in', 'r')
f2=open('1_output.ou', 'w')

init=0
case=1
aliii=int(f.readline())


while case <= aliii:
    
    b=f.readline().replace('\n','').split(' ')
    
    N=int(b[0])
    K=int(b[1])
    m=np.zeros((N,3))
    
    for aux in range(N):
        b=f.readline().replace('\n','').split(' ')
        m[aux,0]=int(b[0])
        m[aux,1]=int(b[1])
        m[aux,2]=2*m[aux,0]*m[aux,1]
    
    
    
    #print m
    b=m[:,2].argsort()[::-1]
    m_sorted=m[b]
    a=m[:,0].argsort()[::-1]
    m=m[a]
    
    
    
    #print m_sorted
   # print a
    #print b
    value_prev=0
    
    
    for aux in range(N):
   
        value=m[aux,0]**2+m[aux,2]
    
        added=1
        for aux2 in range(N):
            if added==K:
                break
            if m_sorted[aux2,0]<=m[aux,0] and a[aux]!=b[aux2]:
                value+=m_sorted[aux2,2] 
               
                added+=1
        
        if value > value_prev:
            value_prev=value
            
        #else:
         #   value_prev=value
    #print m
    print 'Case #'+str(case)+": "+'{0:.16f}'.format(value_prev*np.pi)
    f2.write('Case #'+str(case)+": "+'{0:.16f}'.format(value_prev*np.pi)+'\n')
    case+=1