import string

ifile = open("A-large.in")
fs = ifile.read().split("\n")
ifile.close()

T = int(fs[0])

out = []

NMidx = 1
for t in range(0,T):
    N = int(fs[NMidx].split(" ")[0])
    
    
    wlist = []
    for i in range(1,N+1):
        wlist.append((int(fs[NMidx+i].split(" ")[0]), int(fs[NMidx+i].split(" ")[1])))

    wlist.sort()
    cnt=0
    for i in range(0,N):
        B = wlist[i][1]
        for k in range(i+1,N):
            if wlist[k][1]<B:
                cnt+=1

    out.append("Case #"+str(t+1)+": "+str(cnt))
    NMidx+= (N+1)


ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()