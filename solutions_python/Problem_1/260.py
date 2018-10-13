from numpy import *

f=open('A-large.in','r')
out=open('A-large.out','w')
lines=f.readlines()[:]
k=1
for j in range(int(lines[0][:-1])):
    
    num_engines=int(lines[k][:-1])
    k+=1
    engines=[]
    for i in range(num_engines):
        engines.append(lines[k][:-1])
        k+=1
        
    num_queries=int(lines[k][:-1])
    k+=1
    queries=[]
    for i in range(num_queries):
        queries.append(lines[k][:-1])
        k+=1

    
    p=0
    switch=0
    reste=1
    while reste:
        ePos=[]
        for e in engines:
            if e in queries[p:]:
                ePos.append(queries[p:].index(e))
            else: ePos.append(-1)
        print ePos    

        if -1 in ePos: reste=0
        else:
            p+=max(ePos)
            switch+=1
            
            

    out.writelines('Case #'+str(j+1)+': '+str(switch)+'\n')


out.close()
f.close()
    

    
        

    


    

    

    
