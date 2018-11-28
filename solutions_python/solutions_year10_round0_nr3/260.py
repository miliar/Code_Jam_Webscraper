import glob

for fname in glob.glob("*.in"):
    fin=open(fname, "r")
    fout=open(fname + ".out", "w+")
    output=[]

    for TC in range(1,1+int(fin.readline())):
        R,k,N=[int(x) for x in fin.readline().split()]
        g=[int(x) for x in fin.readline().split()]
        gtmp=[0 for x in range(len(g))]
        gjmp=[0 for x in range(len(g))]

        for i in range(len(g)):
            for j in range(i,min([i+k+1,i+len(g)])):
                ii=gtmp[i]+g[j%len(g)]
                if(ii>k):
                    gjmp[i]=j%len(g)
                    break
                else:
                    gtmp[i]=ii

        j=0
        tot=0
        for i in range(R):
            tot=tot+gtmp[j]
            j=gjmp[j]
        res=tot
        print(g,gtmp,gjmp)
        output.append("Case #%i: %i"%(TC,res))
        
    fin.close()
    fout.write("\n".join(output))
    fout.close()

