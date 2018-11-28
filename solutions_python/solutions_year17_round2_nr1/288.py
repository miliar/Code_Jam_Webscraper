out=open("out.txt","w")
with open("A-large.in") as file: #C-small-practice.in
    T=int(file.readline())
    #print T
    for case in range(T):
        s=file.readline().rstrip()
        D,N=map(int,s.split())
        A=[]
        #print D,N
        if case ==33:
                print D,N
        for i in range(N):

            s=file.readline().rstrip()
            K,S=map(int,s.split())
            #print K,S
            A.append(float(D*S)/float(D-K))
            
        if case==33:
            print A

        ans=min(A)
        #print  str(ans)
        
        
        out.write("Case #"+str(case+1)+": "+str(ans)+"\n")

out.close()