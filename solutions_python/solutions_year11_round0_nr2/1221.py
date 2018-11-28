import sys

f = open(sys.argv[1])

t=int(f.readline().rstrip())

for j in range(1,t+1):
    
    linearr = f.readline().split(" ")
    
    defcombs={}
    defopps={}
    
    ncomb = int(linearr[0])
    for i in range(1,ncomb+1):
        comb = linearr[i]
        defcombs[comb[:-1]]=comb[2]
    
    nopp = int(linearr[ncomb+1])
    for i in range(1,nopp+1):
        comb = linearr[ncomb+1+i]
        
        c1=comb[0]
        c2=comb[1]
        
        if c1 in defopps.keys():
            defopps[c1].append(c2)
        else:
            defopps[c1]=[c2]
        
        if c2 in defopps.keys():
            defopps[c2].append(c1)
        else:
            defopps[c2]=[c1]
            
    n = linearr[ncomb+nopp+2]
    elementlist = linearr[ncomb+nopp+3].strip()
    
    #print defcombs,defopps,n,elementlist
    
    res=[]
    for element in elementlist:
        #import pdb
        #pdb.set_trace()
        res.append(element)
        if len(res)>1:
            last2 = res[-2:]
            comb = defcombs.get(''.join(last2))
            if comb is None:
                last2.reverse()
                comb = defcombs.get(''.join(last2))
            if comb is not None:
                res.pop()
                res.pop()
                res.append(comb)
            else:
                opplist = defopps.get(element)
                if opplist is not None:
                    for oppelem in opplist:
                        if oppelem in res[:-1]:
                            res=[]
                            break
            
    print 'Case #%d: [%s]'%(j,', '.join(res))
    
f.close()
