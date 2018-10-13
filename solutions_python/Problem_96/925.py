f = open('B-large.in')
oo = open('B-large.out','w')

T = int(f.readline())
for cas in range(T):
    data = f.readline().split()
    N = int(data[0])
    S = int(data[1])
    P = int(data[2])
    tp = []
    for i in range(N):
        tp.append(int(data[3+i]))
    tot = 0
    for i in range(N):
        c = tp[i]/3
        r = tp[i] % 3
        if c>=P:
            tot += 1
        elif c+1>=P:
            if r==0 and S>0:
                if tp[i]==0 and P>0:
                    continue
                tot += 1
                S -= 1
            elif r>=1:
                tot += 1
        elif c+r>=P and S>0:
                tot += 1
                S -= 1
    
    oo.write("Case #"+str(cas+1)+": "+str(tot)+'\n')

f.close()
oo.close()
