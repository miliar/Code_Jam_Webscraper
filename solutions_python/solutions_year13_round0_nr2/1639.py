fi = open('B-small-attempt0.in','r')
fo = open('B-small-attempt0.out','w')

nt = int(fi.readline())
for t in range(nt):
    ind = fi.readline().split()
    n = int(ind[0])
    m = int(ind[1])
    ar = []
    bl = []
    for i in range(n):
        ar.append([])
        bl.append([])
        ind = fi.readline().split()
        
        for j in range(m):
            ar[i].append(int(ind[j]))
            bl[i].append(False)
    for i in range(n):
        b = True
        k = ar[i][0]
        for j in range(1,m):
            if ar[i][j] != k:
                b = False
                break
        if b:
            for j in range(m):
                bl[i][j] = True    
    for j in range(m):
        b = True
        k = ar[0][j]
        for i in range(1,n):
            if ar[i][j] != k:
                b = False
                break
        if b:
            for i in range(n):
                bl[i][j] = True
    for i in range(n):
        for j in range(m):
            if not bl[i][j]:
                k = 0
                b = True
                for k in range(n):
                    if not (ar[k][j] == ar[i][j] or (ar[k][j] < ar[i][j] and bl[k][j])):
                        b = False
                        break
                if b:
                    bl[i][j] = True
                    continue
                b = True
                for k in range(m):
                    if not (ar[i][k] == ar[i][j] or (ar[i][k] < ar[i][j] and bl[i][k])):
                        b = False
                        break
                if b:
                    bl[i][j] = True
    for i in range(n):
        b = True
        for j in range(m):
            if not bl[i][j]:
                k = 0
                for k in range(n):
                    if not (ar[k][j] == ar[i][j] or (ar[k][j] == ar[i][j] and bl[k][j])):
                        b = False
                        break
                if b:
                    bl[i][j] = True
                    continue
                b = True
                for k in range(m):
                    if not (ar[i][k] == ar[i][j] or (ar[i][k] == ar[i][j] and bl[i][k])):
                        b = False
                        break
                if b:
                    bl[i][j] = True
                else:
                    break
        if not(b):
            break
    fo.write('Case #'+str(t+1)+': ')
    if b:
        fo.write('YES\n')
    else:
        fo.write('NO\n')
fi.close()
fo.close()