import sys

f = open(sys.argv[1])

count = int(f.readline())

caseidx=1


def prettylist(l):
    res = []
    for el in l:
        res.append( el)
        res.append(', ')
    if res:
        res.pop()
    res.insert(0,'[')
    res.append(']')
    return ''.join(res)

for l in f.readlines():
    its = l.split()

    cC = int(its.pop(0))
    aC = []
    aD = []
    base = {}
    kill = []
    skill = set(kill)
#    print 'its pre cC ', its

    if cC:
        aC = its.pop(0)
        base = { aC[0]+aC[1]:aC[2], aC[1]+aC[0]:aC[2] } 

#    print 'its pre cD ', its
    cD = int(its.pop(0))
#    print 'its post cD ', its
#    print 'cD ', cD
    if cD:
#        print 'cD ', cD
        aD = its.pop(0)
        kill = [ aD[0]+aD[1], aD[1]+aD[0]] 
        skill = set(aD)
#    print 'base, ', base.items()

#    print 'kill, ', kill

    cInv = int(its.pop(0))

    Inv = its.pop()

#    print cInv, Inv

    elist = []

    pos = 0
    idx=0
    def killed(ll):
       # print 'KK ', ll
        if not( skill ):
            return False
        if skill.intersection(ll) == skill:
            return True
        return False
   
    if 0:
        print Inv
        print base
        print kill,skill
 
    while True:
        skip = False
#        if idx < cInv-2:
#            pair =  Inv[idx]+Inv[idx+1]
#            if pair in base:
#                elist.append(base[pair])
#                idx += 2
#                skip = True
#            elif pair in kill:
#            if pair in kill:
#                idx+=2
#                skip = True
#                #elist.append(pair[0])
        
        if not skip:
            elist.append(Inv[idx])
            idx +=1
             
        if len(elist)>=2 :
            pp = elist[-2]+elist[-1]
            if pp in base:
                elist.pop()
                elist.pop()
                elist.append(base[pp])

        if killed(elist):
            elist = []


        if idx == cInv:
            break
 
    print 'Case #%i: ' % caseidx + prettylist(elist)
    caseidx+=1
