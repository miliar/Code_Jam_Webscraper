import re
import math

def ispalin(a):
    arev = int(str(a)[::-1])
    if arev == a:
        return True
    else:
        return False
    
def issqua(a):
    x = a // 2
    seen = set([x])
    while x*x != a:
        x = (x + (a // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True
    
def palin(f):
    with open(f,'r') as ifile:
        case  = int(ifile.readline())
        rlt = []
        for i in range(case):
            line = ifile.readline()
            ni,nf = [z for z in map(int,line.split())]
            cnt = 0
            if ni == 1:
                cnt = 1
                ni = ni + 1
            for i in range(ni,nf+1):
                if ispalin(i) and issqua(i):
                    i_sqrt = int(math.sqrt(i))
                    if ispalin(i_sqrt):
                        cnt = cnt + 1
            rlt.append(cnt)
                        
    with open('output.txt','w') as wfile:
        for i in range(case):
            wfile.write('Case #{0}: {1}\n'.format(i+1, rlt[i]))               
                
if __name__ == '__main__':
    import sys
    f = sys.argv[1]
    palin(f)
