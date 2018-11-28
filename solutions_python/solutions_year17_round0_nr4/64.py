q = int(input())
for case in range(1,q+1):
    n,m = [int(x) for x in input().split()]
    
    cols = [0]*n
    rows = [0]*n
    
    firstrow_plus = [0]*n
    
    orgmatrix = [[0]*n for _ in range(n)]
    matrix = [[0]*n for _ in range(n)]
    
    backwards = [0]*(2*n-1)
    forwards = [0]*(2*n-1)

    points = 0
    for _ in range(m):
        c,b,a = input().split()
        a = int(a)-1
        b = int(b)-1
        if c == 'x' or c == 'o':
            cols[a] += 1
            rows[b] += 1
            points += 1
            orgmatrix[b][a] += 1
        if c == '+' or c == 'o':
            c1,c2 = a+b,a-b
            backwards[c2]+=1
            forwards[c1]+=1

            firstrow_plus[a] += 1
            points += 1
            orgmatrix[b][a] += 2
    
    numbackwards = [0]*(2*n-1)
    numforwards = [0]*(2*n-1)
    
    for i in range(n):
        for j in range(n):
            c1,c2 = i+j,i-j
            numbackwards[c2]+=1
            numforwards[c1]+=1

    def cover(pos):
        i,j = pos
        c1,c2 = i+j,i-j
        return numbackwards[c2] + numforwards[c1]
    
    poi = [(i,j) for i in range(n) for j in range(n)]
    poi.sort(key = lambda x: cover(x))

    for pos in poi: 
        i,j = pos
        c1,c2 = i+j,i-j

        if backwards[c2]== 0 and forwards[c1] == 0:
            matrix[j][i] += 2
            points += 1
            backwards[c2]+=1
            forwards[c1]+=1

    i = 0
    j = 0
    while i < n and j < n:
        while i < n and rows[i]>0:
            i+=1
        while j<n and cols[j]>0:
            j+=1
        if i >= n or j >= n:
            continue
        rows[i] += 1
        cols[j] += 1
        matrix[i][j] += 1
        points += 1








    #for j in range(n):
    #    if firstrow_plus[j] == 0:
    #        matrix[0][j] += 2
    #        points += 1

    #for j in range(1,n-1):
    #    matrix[n-1][j] += 2
    #    points += 1
    
    changes = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j]>0:
                changes += 1

    print('Case #%d: %d %d' %(case,points,changes))
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==1:
                if orgmatrix[i][j]>0:
                    print('o %d %d' %(i+1,j+1))
                else:
                    print('x %d %d' %(i+1,j+1))
            elif matrix[i][j]==2:
                if orgmatrix[i][j]>0:
                    print('o %d %d' %(i+1,j+1))
                else:
                    print('+ %d %d' %(i+1,j+1))
            elif matrix[i][j]>2:
                print('o %d %d' %(i+1,j+1))
   
    #prmat = [['.']*n for _ in range(n)]
    #for i in range(n):
    #    for j in range(n):
    #        dumhet = matrix[i][j] + orgmatrix[i][j]
    #        if dumhet == 1: 
    #            prmat[i][j] = 'x'
    #        elif dumhet == 2:
    #            prmat[i][j] = '+'
    #        elif dumhet == 3:
    #            prmat[i][j] = 'o'
    #for i in range(n):
    #    print(*prmat[i])
