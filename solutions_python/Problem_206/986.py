fname="A-large.in"
f=open(fname)
f.readline()
T=1
g = open("output.out", "w")

cases=f.readlines()
i=0
while i<len(cases):
    res=0
    
    D=float(cases[i].strip().split()[0])
    N=int(cases[i].strip().split()[1])
    K=[]
    S=[]
    
    for aux in xrange(i+1,i+N+1):
        K.append(float(cases[aux].strip().split()[0]))
        S.append(float(cases[aux].strip().split()[1]))
        
    print D,N,K,S
     
    
    K.reverse()
    S.reverse()
    
    t=0
    for aux in xrange(len(K)):
        t_aux=(D-K[aux])/S[aux]
        
        if t_aux>t:
            t=t_aux
            
    res=D/t
    
    i+=N+1
    
    
    
    print 'Case #'+str(T)+': ' + str(res) +'\n'
    g.write('Case #'+str(T)+': ' + str(res) +'\n')
    T+=1 