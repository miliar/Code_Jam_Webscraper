

fout = open('out.txt','w')
f = open('in.txt')

T = int(f.readline())
for case in range(1,T+1):
    line = f.readline()


    line = line.split()
    nc = int(line[0])
    nj = int(line[1])

    c = []
    sc = 0
    for i in range(nc):
        line = f.readline()
        line = line.split()
        start = int(line[0])
        end = int(line[1])
        c.append((start,end,0))
        sc += end-start

    j = []
    sj = 0
    for i in range(nj):
        line = f.readline()
        line = line.split()
        start = int(line[0])
        end = int(line[1])
        j.append((start,end,1))
        sj += end-start

    all = c + j
    all.sort(key = lambda x:x[0])
    q,w,e = all[0]
    all.append((q+24*60,w+24*60,e))

    gaps = []
    ans = 0
    for i in range(len(all)-1):
        if all[i][2] == all[i+1][2]:
            gaps.append((all[i][1], all[i+1][0], all[i][2]))
        else:
            ans += 1
    
    gaps.sort(key = lambda g: g[1]-g[0])
    for g in gaps:
        if g[2] == 0:
            sc += g[1]-g[0]
            if sc > 12*60:
                ans += 2
        if g[2] == 1:
            sj += g[1]-g[0]
            if sj > 12*60:
                ans += 2
    
    ans = max(ans,2)
    
    str = "Case #%d: %s\n" % (case, ans)
    print str,
    fout.write(str)

f.close()
fout.close()
