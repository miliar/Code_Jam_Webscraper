import string

ifile = open("A-large.in")
fs = ifile.read().split("\n")
ifile.close()

T = int(fs[0])

out = []

NMidx = 1
for t in range(0,T):
    N = int(fs[NMidx].split(" ")[0])
    M = int(fs[NMidx].split(" ")[1])
    
    #already exist
    da = dict()
    for i in range(NMidx+1,NMidx+1+N):
        spl = fs[i].split("/")[1:]
        path=""
        for s in spl:
            path = path+"/"+s
            da[path]=1

    #req
    mdcnt = 0
    for i in range(NMidx+1+N,NMidx+1+N+M):
        spl = fs[i].split("/")[1:]
        path=""
        for s in spl:
            path = path+"/"+s
            if not path in da:
                da[path] = 1
                mdcnt+=1

    out.append("Case #"+str(t+1)+": "+str(mdcnt))
    NMidx+= (N+M+1)


ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()