import string

ifile = open("C-small-attempt0.in")
fs = ifile.read().split("\n")
ifile.close()

C = int(fs[0])

out = []

NMidx = 1
for t in range(0,C):

    R = int(fs[NMidx].split(" ")[0])
    rec = []
    for i in range(1,R+1):
        rec.append([int(x) for x in (fs[NMidx+i].strip().split(" "))])
    
    #find max
    size = 0
    for i in rec:
        for k in i:
            if k > size:
                size = k

    size +=1
    #make grid
    G1 = [xx[:] for xx in [[0]*(size)]*(size)]
    G2 = [xxx[:] for xxx in [[0]*(size)]*(size)]

    #gen bact
    for i in rec:
        for y1 in range(i[1],i[3]+1):
            for x1 in range(i[0],i[2]+1):
                G1[y1][x1] = 1
    G=[G1,G2]

    
    cnt = 0
    while True:
        ori = cnt%2
        cpy = (cnt+1)%2
        is_any=False
        
        for y in range(1,size):
            for x in range(1,size):
                if G[ori][y][x] == 1:
                    if (G[ori][y-1][x] == 0) and (G[ori][y][x-1]==0):
                        G[cpy][y][x] = 0
                    else:
                        G[cpy][y][x] = 1
                        is_any = True                        
                else:# empty cell case
                    if G[ori][y-1][x] == 1 and G[ori][y][x-1]==1:
                        G[cpy][y][x] = 1
                        is_any = True
                    else:                        
                        G[cpy][y][x] = 0
        cnt+=1
        if not is_any:
            break;

    out.append("Case #"+str(t+1)+": "+str(cnt))
    NMidx+= R+1 


ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()