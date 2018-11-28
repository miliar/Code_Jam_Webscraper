#!/usr/bin/env python
import sys

def cal(R, C, arr):
    for r in range(R):
        for c in range(C):
            cell = arr[r][c]
            if cell == '#':
                if (r==R-1 or arr[r+1][c]!='#'):
                    return False
                if (c==C-1 or arr[r][c+1]!='#'):
                    return False
                if arr[r+1][c+1]!='#':
                    return False
                arr[r][c] = '/'
                arr[r][c+1] = '\\'
                arr[r+1][c] = '\\'
                arr[r+1][c+1] = '/'
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
        f.write('Case #%d: \n%s\n'%(i+1,r))
    f.close()

def rf(fileName):
    f = open(fileName,'r')
    inputs = []
    n = int(f.readline())
    for i in range(n):
        l = f.readline()
        l=l.split()
        R=int(l[0])
        C=int(l[1])
        arr = []
        for j in range(R):
            arr.append(list(f.readline().strip()))
        inputs.append((R,C,arr))
    return inputs
   
if __name__=='__main__':
    fn = sys.argv[-1]
    inputs = rf(fn)

    results = []
    for R,C,arr in inputs:
        rt = cal(R, C, arr)
        print rt 
        if rt:
            arr = [''.join(l) for l in arr]
            results.append('\r'.join(arr))
        else:
            results.append('Impossible')
    wf(fn[:-2]+'out',results)

