def solveB(D,H,curH,pos,cur_t):
    if pos==N-2:
        if D[N-1]-D[N-2]<=curH[0]:
            tm1=float(D[N-1]-D[N-2])/curH[1]
        else:
            tm1=10**10
        if D[N-1]-D[N-2]<=H[N-2][0]:
            tm2=float(D[N-1]-D[N-2])/H[N-2][1]
        else:
            tm2=10**10
            
        return cur_t+min(tm1,tm2)
        
    t1,t2=-1,-1
    if D[pos+1]-D[pos]<=curH[0]:
        tm1=float(D[pos+1]-D[pos])/curH[1]
        new_E=curH[0]-(D[pos+1]-D[pos])
        t1=solveB(D,H,[new_E,curH[1]],pos+1,cur_t+tm1)
    
    if D[pos+1]-D[pos]<=H[pos][0]:
        tm2=float(D[pos+1]-D[pos])/H[pos][1]  
        new_E=H[pos][0]-(D[pos+1]-D[pos])
        t2=solveB(D,H,[new_E,H[pos][1]],pos+1,cur_t+tm2)
        #print pos

    if t1>-1:
        if t2>-1:
            return min(t1,t2)
        else:
            return t2
    else:
        return t2
        
    return 0
    

out=open("out.txt","w")
with open("C-small-attempt1.in") as file: #C-small-practice.in
    T=int(file.readline())
    #print T
    for case in range(T):
        print "case: ",case
        s=file.readline().rstrip()
        N,Q=map(int,s.split())
        D=[0]*N
        H=[]
        for i in range(N):
            s=file.readline().rstrip()
            E,S=map(int,s.split())
            H.append([E,S])
        for i in range(N):
            s=file.readline().rstrip().split()
            #print s, s[i+1],i
            #s=map(int,s)
            if i<N-1:
                D[i+1]=D[i]+int(s[i+1])
        print D
        MT=[10**20]*N
        MT[0]=0
        for i in xrange(Q):
            s=file.readline().rstrip()
            #print s
            U,V=map(int,s.split())
        #print min(A)
        #ans= solveB(D,H,H[0],0,0)
        for pos in xrange(N):
            for i in xrange(pos+1,N):
                if D[i]-D[pos]<=H[pos][0]:
                    ti=float(D[i]-D[pos])/H[pos][1]
                    MT[i]=min(MT[i],MT[pos]+ti)
        ans=MT[N-1]
        print ans
        
        out.write("Case #"+str(case+1)+": "+str(ans)+"\n")

out.close()