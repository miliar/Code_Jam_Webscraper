f=open('B-large.in')
lines = []
for line in f.readlines():
        lines.append(line)
f.close()
a = lines.pop(0)
T = int(a)
for case in range(T):
        a = lines.pop(0)
        [n,m] = (a.strip()).split()
        N = int(n)
        M = int(m)
        hight = []
        if N<=1 or M<=1:
                ans = 'YES'
                for i in range(N):
                        lines.pop(0)
                print('Case #',case+1,': ',ans,end='\n',sep='')
                continue
        else:
                hight =[]*N
                for i in range(N):
                        line = lines.pop(0)
                        a = (line.strip()).split()
                        hs =[]
                        for h in a:
                                hs.append(int(h))
                        hight.append(hs)
        con = []
        for hs in hight:
                for h in hs:
                        if h not in con:
                                con.append(h)
        con.sort()
        ans = 'YES'
        for m in con:
                #init mask
                mask = [[ (i <= m ) for i in hs] for hs in hight]
                for j,hs in enumerate(hight):
                        if ( max(hs) <= m ):
                                mask[j] = [False for i in hs ]
                for k in range(M):
                        hsx = []
                        for hs in hight:
                                hsx.append(hs[k])
                        if ( max(hsx) <= m ):
                                for i in range(N):
                                        mask[i][k] = False
                for ms in mask:
                        for s in ms:
                                if s:
                                        ans = 'NO'
                                        break
        print('Case #',case+1,': ',ans,end='\n',sep='')
                
        
                
               
