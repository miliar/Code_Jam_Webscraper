t=input()
for i in range(t):
    n=raw_input()
    nlist=list(n)
    nsort=nlist[:]
    nsort.sort()
    if nsort==nlist:
        print "Case #%d: %s" %(i+1, n)
    else:
        nnew=[]
        j=0
        while int(nlist[j])<=int(nlist[j+1]):
            j+=1
        if j==0:
            nnew.append(str(int(nlist[0])-1))
            for z in range(len(n)-1):
             nnew.append("9")
        else:
            k=1
            while (j-k)>=0:
                if nlist[(j-k)]==nlist[j]:
                    k+=1
                else:
                    break
            for z in range(j-k+1):
                nnew.append(nlist[z])
            nnew.append(str(int(nlist[j-k+1])-1))
            for z in range(len(n)-j+k-2):
                nnew.append("9")
        if nnew[0]=="0":
            nnew=nnew[1:]
        nnew2="".join(nnew)
        print "Case #%d: %s" %(i+1, nnew2)
            
