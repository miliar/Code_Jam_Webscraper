
fp = open('D-large.in')
out = open('D-out.txt','w')
def play(As,Bs):
    As.sort()
    Bs.sort()
    S = set(Bs)
    ret = 0
    for x in As:
        cand = sorted(filter(lambda y:y>x,S))
        if len(cand)==0:
            ret+=1
            S.remove(min(S))
        else:
            S.remove(cand[0])
    return ret

def playd(As,Bs):
    As.sort()
    Bs.sort()
    S = set(Bs)
    ret = 0
    for x in As:
        cand = sorted(filter(lambda y:y<x,S),reverse=True)
        if len(cand)==0:
            S.remove(max(S))
        else:
            ret+=1
            S.remove(cand[0])
    return ret


T = int(fp.readline())
casno = 1
while T!=0:
    T-=1
    n = int(fp.readline())
    As = map(float,fp.readline().split())
    Bs = map(float,fp.readline().split())
    out.write('Case #%d: ' % casno)
    Aw = playd(As,Bs)
    Bw = play(As,Bs)
    print As,Bs
    print Aw,Bw
    out.write('%d %d\n' % (Aw,Bw))
    casno +=1 
