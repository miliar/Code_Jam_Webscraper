# -*- coding: utf-8 -*-
fname = "B-large"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

numcases = gcj_read()[0]

for caseno in range(numcases):
    l = fin.readline().strip().split()
    C = int(l[0])
    combinestrs = l[1:C+1]
    D = int(l[C+1])
    opposingstrs = l[C+2:C+2+D]
    invoked = l[-1]
    
    combines = {}
    for a, b, r in combinestrs:
        combines[(a,b)] = r
        combines[(b,a)] = r
    opposing = [set([a,b]) for a, b in opposingstrs]
    print combines, opposing, invoked
    
    elist = []
    for e in invoked:
        # Empty list - just add
        if not elist:
            elist.append(e)
            continue
        
        # Check combining
        tocombine = (elist[-1], e)
        if tocombine in combines:
            elist[-1] = combines[tocombine]
        else:
            elist.append(e)
        
        # Check opposing
        eset = set(elist)
        for opppair in opposing:
            if opppair.issubset(eset):
                elist = []
                break
            
    
    
    outstr = "[" + ", ".join(elist) + "]"
    print outstr
    fout.write("Case #"+str(caseno+1)+": "+ outstr +"\n")

fin.close()
fout.close()
