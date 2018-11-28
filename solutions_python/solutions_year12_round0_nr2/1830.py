
f = open(r'c:\B-small-attempt0.in')
of = open(r'c:\a.out','w')
c = int(f.readline().strip())
for i in range(c):
    line = [int(s) for s in f.readline().strip().split(' ')]
    N,S,p = line[0],line[1],line[2]
    scores = line[3:]
    num = 0
    for score in scores:
        if score < p:
            pass
        elif (score-p)//2 + 2 > p:
            num+=1
        elif (score-p)//2 + 2 == p:
            if S>0:
                num+=1
                S-=1
    print('Case #%d: %d'%(i+1,num), file=of)
of.close()
f.close()
