def main():
    T = int(raw_input())
    for case in range(T):
        blocks=int(raw_input())
        naomi=[]
        ken=[]
        temp1=raw_input().split()
        temp2=raw_input().split()
        for i in temp1:
            naomi.append(float(i))
        for i in temp2:
            ken.append(float(i))
        print 'Case #%d: %d %d'%(case+1,deceitwar(naomi,ken,blocks),war(naomi,ken,blocks))

def war(naomi,ken,blocks):
    naomi=naomi[:]
    ken=ken[:]
    score=0
    for i in range(blocks):
        naomic=max(naomi)
        naomi.remove(naomic)
        kenc=max(ken)
        if naomic>kenc:
            kenc=min(ken)
            ken.remove(kenc)
        else:
            ken.remove(kenc)
        if naomic>kenc:
            score+=1

    return score

def deceitwar(naomi,ken,blocks):
    score=0
    naomi=naomi[:]
    ken=ken[:]
    for times in range(blocks):
        kenmax = max(ken)
        naomimax=max(naomi)
        l=[ a for a in naomi if a > kenmax]
        if len(l) > 0:
            naomic=min(l)
            naomi.remove(naomic)
            ken.remove(kenmax)
            score+=1
        else:
            naomic=min(naomi)
            naomi.remove(naomic)
            ken.remove(kenmax)
    return score




if __name__=='__main__':
    main()
