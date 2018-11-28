#!/usr/bin/env python
import sys

def getMaxDivider(x,y):
    if x==0 or y==0:
        return 0
    m = x%y
    if m==0:
        return y
    else:
        return getMaxDivider(y,m)

def cal(N, Pn, Pg):
    PnD = getMaxDivider(Pn, 100)
    if PnD == 0:
        PnD = 100
    Pn1 = Pn/PnD
    Pn2 = 100/PnD
    if N<Pn2:
        return False
    if Pn!=100 and Pg==100:
        return False
    if Pn!=0 and Pg==0:
        return False
    return True

    PgD = getMaxDivider(Pg, 100)
    if PgD == 0:
        PgD = 100
    Pg1 = Pg/PgD
    Pg2 = 100/PgD
    scale = round(Pg2*1.0/Pn2)
    Pg1 *= scale
    Pg2 *= scale
    if Pg2-Pn2<Pg1-Pn1:
        return False
    return True
    
def wf(fileName,results):
    f = open(fileName,'w')
    for i,r in enumerate(results):
        f.write('Case #%d: %s\n'%(i+1,r))
    f.close()

def rf(fileName):
    f = open(fileName,'r')
    inputs = []
    n = int(f.readline())
    for i in range(n):
        l = f.readline()
        inputs.append(l.split())
    return inputs
   
if __name__=='__main__':
    fn = sys.argv[-1]
    inputs = rf(fn)

    results = []
    for N,Pn,Pg in inputs:
        rt = cal(int(N), int(Pn), int(Pg))
        print rt 
        if rt:
            results.append('Possible')
        else:
            results.append('Broken')
    wf(fn[:-2]+'out',results)

