f=open("B-large.in")
g=open("outB","w")
cases=int(f.readline())
def col(a,b,stri):
    ans[a][b]=stri
    for c in connected[a][b]:
        col(c[0],c[1],stri)
for i in xrange(1,cases+1):
    hw=map(int,f.readline().split())
    sinks=[]
    terrain=[]
    lolful=[]
    for j in xrange(hw[1]+2):
        lolful.append(10000)
    terrain.append(lolful)
    for j in xrange(hw[0]):
        p=[10000]
        p+=(map(int,f.readline().split()))
        p.append(10000)
        terrain.append(p)
    terrain.append(lolful)
    connected=[]
    ans=[]
    sinks=[]
    for j in xrange(hw[0]+2):
        line=[]
        for k in xrange(hw[1]+2):
            line.append("hooh")
        ans.append(line)
    for j in xrange(hw[0]+2):
        line=[]
        for k in xrange(hw[1]+2):
            line.append([])
        connected.append(line)
    for h in xrange(1,hw[0]+1):
        for w in xrange(1,hw[1]+1):
            if terrain[h][w]<=min(terrain[h-1][w],terrain[h+1][w],terrain[h][w+1],terrain[h][w-1]):
                sinks.append([h,w])
            else:
                for x in [[-1,0],[0,-1],[0,1],[1,0]]:
                    if terrain[h+x[0]][w+x[1]]==min(terrain[h-1][w],terrain[h+1][w],terrain[h][w+1],terrain[h][w-1]):
                        connected[h+x[0]][w+x[1]].append([h,w])
                        break

    for thing in xrange(len(sinks)):
        col(sinks[thing][0],sinks[thing][1],chr(thing+97))

    dictlist=[]
    for tr in xrange(26):
        dictlist.append("hello")
    counter=97
    for h in xrange(1,hw[0]+1):
        for w in xrange(1,hw[1]+1):
            if dictlist[ord(ans[h][w])-97]=="hello":
                dictlist[ord(ans[h][w])-97]=chr(counter)
                counter+=1
            ans[h][w]=dictlist[ord(ans[h][w])-97]

    g.write( "Case #"+str(i)+":\n")
    for line in xrange(1,hw[0]+1):
            ansln=""
            for chara in xrange(1,hw[1]+1):
                ansln+=ans[line][chara]+" "
            g.write( ansln.rstrip()+"\n")
f.close()
g.close()
