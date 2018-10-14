#Read input file with extension .in
#for path in files:
#    if path.find('.in') != -1:
#        break
#print path
name ='D-large'
f = open(name+'.in')
o = open(name+'.out','w')
cases=int(f.readline())

for case in xrange(1,cases+1):
    Nblocks = int(f.readline())
    naomi = [float(z) for z in f.readline().strip().split(' ')]
    ken = [float(z) for z in f.readline().strip().split(' ')]
    naomi.sort()
    ken.sort()
    cnaomi = naomi[:]
    cken = ken[:]
    score=0
    while naomi: #deceival
        Nmin = naomi[0]
        Kmin = ken[0]
        Kmax = ken[-1]
        if Nmin > Kmax:
            score += len(naomi)
            break
        elif Nmin > Kmin:
            score+=1
            del naomi[0]
            del ken[0]
        else:
            del naomi[0]
            del ken[-1]
    #war
    wscore=0
    while cnaomi:
        w = cnaomi.pop()
        Kmin = cken[0]
        Kmax = cken[-1]
        if w>Kmax:
            wscore+=1
            del cken[0]
        elif w<Kmin:
            break
        else:
            for i in xrange(len(cken)-1,-1,-1):
                if cken[i]<w:
                    i+=1
                    break
            del cken[i]
    o.write('Case #%d: %d %d\n' % (case,score,wscore))

f.close()
o.close()
