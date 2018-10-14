filename = 'D-large.in' #raw_input()

def DeceitfulWar(_naomis,_kens):
    naomis = _naomis[:]
    kens = _kens[:]
    score=0
    naomis.sort()
    kens.sort()
    #print len(naomis)
    #print naomis
    #print kens
    while len(naomis) > 0 and len(kens) > 0:
        if naomis[0] > kens[0] :
            score += 1
            del naomis[0]
            del kens[0]
        else:
            del naomis[0]
            del kens[-1]
    return score

def War(_naomis,_kens):
    naomis = _naomis[:]
    kens = _kens[:]
    score=0
    naomis.sort()
    kens.sort()
    while len(naomis) > 0 and len(kens) > 0:
        if naomis[-1] > kens[-1]:
            score += 1
            del naomis[-1]
            del kens[0]
        else:
            for i in range(len(kens)):
                if kens[i] > naomis[-1]:
                    del kens[i]
                    break
            del naomis[-1]
    return score

with open (filename) as f:
    T = int(f.readline())
    for icase in range(T):
        n = int(f.readline())
        naomis = [float(a) for a in f.readline().split() ]
        kens = [float(a) for a in f.readline().split() ]
        print 'Case #%s: %s %s' % (icase+1, DeceitfulWar(naomis,kens), War(naomis,kens))
        
        