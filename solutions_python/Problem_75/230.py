#!/usr/bin/python

import sys

for n,line in enumerate(open(sys.argv[1])):
    if n==0:
        continue
    te=line.split()
    
    combnum=int(te[0])
    combl=te[1:combnum+1]
    oppnum=int(te[combnum+1])
    oppl =te[(combnum+2):(combnum+oppnum+2)]
    qs=te[-1]
    
    comb={(s[0],s[1]):s[2] for s in combl}
    comb.update({(s[1],s[0]):s[2] for s in combl})
    opp={}
    for s in oppl:
        if not s[0] in oppl:
            opp[s[0]]=set(s[1])
        else:
            opp[s[0]].add(s[1])
        if not s[1] in oppl:
            opp[s[1]]=set(s[0])
        else:
            opp[s[1]].add(s[0])
    
    ans=""
    skip=False
    for i in range(0,len(qs)):
        if i > 0 and len(ans) > 0 and (ans[-1],qs[i]) in comb:
            ans = ans[:-1]+comb[(ans[-1],qs[i])]
        else:
            if qs[i] in opp:
                for c in opp[qs[i]]:
                    f = ans.rfind(c)
                    if f != -1:
                        ans=""
                        break
                else:
                    ans+=qs[i]
            else:
                ans+=qs[i]

        #print(qs[i],ans)
        
    #print(comb,opp,qs,ans)

    
    print("Case #{0}: [{1}]".format(n,", ".join([c for c in ans])))

