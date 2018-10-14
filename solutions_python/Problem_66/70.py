import string

ifile = open("B-small-attempt0.in")
fs = ifile.read().split("\n")
ifile.close()

T = int(fs[0])

out = []

NMidx = 1
for t in range(0,T):
    P = int(fs[NMidx])
    M = [int(x) for x in (fs[NMidx+1].strip().split(" "))]
    
    C = []
    for i in range(0,P):
        C.append([[int(x),False] for x in (fs[NMidx+2+i].strip().split(" "))])

    teamidx =0
    for miss in M:
        #mark along m
        treeidx = teamidx
        for i in range(0,miss+1):
            treeidx/=2
        i=miss
        while i<P:
            C[i][treeidx][1] = True #buy
            i+=1
            treeidx/=2
        teamidx+=1    

    #cal money
    money = 0
    for i in C:
        for k in i:
            if k[1]==True:
                money+=k[0]

    out.append("Case #"+str(t+1)+": "+str(money))
    NMidx+= P+2


ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()