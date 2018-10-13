# -*- coding: utf-8 -*-
fname = "B-small-attempt0"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

numcases = gcj_read()[0]

from math import log2

for caseno in range(numcases):
    N, P = gcj_read()
    teams = 2**N
    
    mustwin, canwin = 0, 0
    
    for teamno in range(teams):
        posslose = int(log2(teamno+1))
        posswin = int(log2(teams-teamno))
        bestseq = ('0' * posswin) + ('1' * (N-posswin))
        bestplace = int(bestseq, 2)
        worstseq = ('1' * posslose) + ('0' * (N-posslose))
        worstplace = int(worstseq, 2)
        
        if bestplace < P:
            canwin = teamno
        if worstplace < P:
            mustwin = teamno
        
        #print(teamno, bestseq, worstseq)
        print(teamno, bestplace, worstplace)
    
    outstr = '%d %d' % (mustwin, canwin)
    
    print("Case #"+str(caseno+1)+": "+ outstr)
    fout.write("Case #"+str(caseno+1)+": "+ outstr +"\n")

fin.close()
fout.close()
