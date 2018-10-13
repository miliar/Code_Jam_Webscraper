import math

def dfs(N,S,P,t):
   # print t
    q=[]
    q.append((S,-1,0))
    maxV=-1
    while(len(q)!=0):
        #print q
        c=q.pop()
        
        #print c
        if c[1]==N-1:
            if c[0]==0:
                maxV=max(maxV,c[2])
            continue
        
        shifts=[-2,-1,0,1,2]
        
        cTop=t[c[1]+1]
        #print cTop
        
        p1s=cTop/3
        
        pshifts=[-1,0,1]
        for a in pshifts:
            p1=p1s+a
            if p1<0 or p1>10: 
                    continue
            
            for x in shifts:
                p2=p1s+x
                p3=cTop-p1-p2
                if p2<0 or p2>10 or p3<0 or p3>10: 
                    continue

                delta=0
                if p1>=P or p2>=P or p3>=P :
                    delta=1
                
                
                if math.fabs(p3-p1)<=1 and math.fabs(p3-p2)<=1 and math.fabs(p1-p2)<=1:
         #          print 't',p1,p2,p3
                    q.append((c[0],c[1]+1,c[2]+delta))
                elif math.fabs(p3-p1)<=2 and math.fabs(p3-p2)<=2 and math.fabs(p1-p2)<=2 and c[0]>0:
          #          print 't',p1,p2,p3
                    q.append((c[0]-1,c[1]+1,c[2]+delta))
#                elif math.fabs(p3-p1)<=2 and math.fabs(p3-p2)==2and c[0]>0:
#                    q.append((c[0]-1,c[1]+1,c[2]+delta))
                    
    
    return maxV        
   
    



f = open('B-small-attempt0.in', 'r')
T=int(f.readline())
totalOut=''
for i in range(1,T+1):
    S= f.readline()
    if (('\n') in S):
        S=S[:-1]
    lst=S.split(' ')
    N=int(lst[0])
    S=int(lst[1])
    P=int(lst[2])
    lst=lst[3:]
    t=map(int,lst)
    
                
    totalOut+= 'Case #'+str(i)+': '+str(dfs(N,S,P,t))+'\n'
totalOut=totalOut[:-1]
#print totalOut
outD= open ('B-small-attempt0.out','w')
outD.write(totalOut)