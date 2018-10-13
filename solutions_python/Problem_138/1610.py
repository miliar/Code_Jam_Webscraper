'''
Created on 2014-04-11

@author: Tiger
'''
def getDeceit(n,k,t):
    scoreN=0
    scoreK=0
 
    for i in range(t):
        n1 = min(n)
        if min(k)<n1:
            k1 = min(k)
        elif n1 < max(k):
            k1 = max(k)
        else:
            t=[]
            for x in k:
                if x <n1:
                    t.append(x)
            k1 = min(t)
        
        if float(n1) > float(k1) :
            scoreN+=1
        else:
            scoreK+=1
            
        n.remove(n1)
        k.remove(k1)
    
    return scoreN

def getFair(n,k,t):
    scoreN=0
    scoreK=0
   
    for i in range(t):
        n1 = min(n)
        if n1 > max(k):
            k1 = min(k)
        else:
            t =[]
            for x in k :
                if x >n1:
                    t.append(x)
            
            k1 = min(t)
        
        if float(n1) > float(k1) :
            scoreN+=1
        else:
            scoreK+=1
        n.remove(n1)
        k.remove(k1)
    
    return scoreN

f = open ("D-large.in","r")
case =1
tests = f.readline().strip()
for i in range(int(tests)):
    t = int(f.readline().strip())
    N =f.readline().strip().split()
    K =f.readline().strip().split()
    n1 = N[:]
    k1 = K[:]

    fai = getFair(n1,k1,t)

    dec= getDeceit(N,K,t)
    print "Case #"+str(case)+":", dec,fai
    
   
    case+=1