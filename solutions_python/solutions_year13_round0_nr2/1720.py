import re

def lawn(f):
    with open(f,'r') as ifile:
        case  = int(ifile.readline())
        rlt = []
        for i in range(case):
            line = ifile.readline()
            n,m = [z for z in map(int,line.split())]
            klist = []
            for j in range(n):
                line = ifile.readline()
                vec = [z for z in map(int,line.split())]
                klist.append(vec)
            minvec = []
            for j in range(n):
                minvec.append(min(klist[j]))
            minum = min(minvec)
            clist = []
            for j in range(m):
                vec = []
                for k in range(n):
                    vec.append(klist[k][j])
                clist.append(vec)
            cnt = 0
            for k,j in [(k,j) for k in range(n) for j in range(m)]:
                if klist[k][j] == minum:
                    if max(klist[k]) > minum and max(clist[j]) > minum:
                        cnt = cnt + 1
            if cnt == 0:
                rlt.append('YES')
            else:
                rlt.append('NO')
                    
                        
                        
                        
    with open('lawn.txt','w') as wfile:
        for i in range(case):
            wfile.write('Case #{0}: {1}\n'.format(i+1, rlt[i]))               
                
if __name__ == '__main__':
    import sys
    f = sys.argv[1]
    lawn(f)
