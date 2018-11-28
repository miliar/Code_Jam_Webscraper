def problemA(R,C,G):
    for i in xrange(C):
        for j in xrange(R):
            if G[j][i]<>'?':
                for k in xrange(j-1,-1,-1):
                    if G[k][i]=='?':
                        G[k][i]=G[j][i]
                    else:
                        break
                for k in xrange(j+1,R):
                    if G[k][i]=='?':
                        G[k][i]=G[j][i]
                    else:
                        break
            
    for i in xrange(C):
        for j in xrange(R):
            if G[j][i]<>'?':
                for k in xrange(i-1,-1,-1):
                    if G[j][k]=='?':
                        G[j][k]=G[j][i]
                    else:
                        break
                for k in xrange(i+1,C):
                    if G[j][k]=='?':
                        G[j][k]=G[j][i]
                    else:
                        break                    
    return G

out=open("out.txt","w")
with open("A-large.in") as file: #A-large.in
    T=int(file.readline())
    #print T
    for case in range(T):
        s=file.readline().rstrip()
        R,C=map(int,s.split())
        G=[['?']*C for i in xrange(R)]
        for i in xrange(R):
            s=file.readline().rstrip()
            G[i]=[s[j] for j in xrange(C)]
        
        ans=problemA(R,C,G)
        
        out.write("Case #"+str(case+1)+":\n")
        for i in range(R):
            out.write("".join([G[i][j] for j in xrange(C)])+"\n")

out.close()