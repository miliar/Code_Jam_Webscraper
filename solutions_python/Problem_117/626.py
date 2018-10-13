def row(a,M,N):
    rn = a/M
    c = []
    for p in range(rn * (M), (rn+1) * M):
        c.append(p)
    return c

def col(a,M,N):
    cn = a % M
    c = []
    for p in range(0,N):
        c.append(p*M + cn)
    return c

#A = [[2,2,2,2,2],[2,1,1,1,2],[2,1,1,1,2],[2,1,1,1,2],[2,2,2,2,2]]

#A = [[2,2,2,2,2],[2,1,1,1,2],[2,1,1,1,2],[2,1,1,1,2],[2,2,2,2,2]]

f = open('B-small-attempt3.in','r')
T = f.readline()
T = int(T[0:-1])

for TC in range(0,T):
    CC = f.readline()
    [N,M] = CC.split()
    N = int(N)
    M = int(M)
    c = 0
    d = set()
    for i in range(0,N):
        CC = f.readline()
        CC2 = CC.split()
        for j in CC2:
            if j == '1':
                d.add(c)
            c += 1
#A = [[1,2,1,2,2],[1,2,1,2,2],[1,1,1,1,1],[1,2,1,2,2],[1,1,1,1,1]]
#N = 5
#M = 5

#c = 0
#d = set()
#for x in A:
#    for y in x:
#        if y == 1:
#            d.add(c)
#        c += 1

    allc = True
    for e in d:
        rowc = True
        colc = True
        
        rr = row(e,M,N)
        cc = col(e,M,N)
        for rrr in rr:
            if rrr not in d:
                rowc = False
                break
        for ccc in cc:
            if ccc not in d:
                colc = False
                break
        if rowc == False and colc == False:
            allc = False
            break
    
    if allc == False:
        print('Case #' + str(TC+1) + ': NO')
    else:
        print('Case #' + str(TC+1) + ': YES')
