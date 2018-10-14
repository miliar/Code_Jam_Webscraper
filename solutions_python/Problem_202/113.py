T = int(raw_input())

for i in xrange(T):
    u, v = map(int, raw_input().split())
    mat1 = [['.'] * u for k in xrange(u)]
    mat2 = [['.'] * u for k in xrange(u)]
    col = [0] * u
    row = [0] * u
    diag = [0] * (2 * u - 1)
    adiag = [0] * (2 * u - 1)
    ans = 0
    for j in xrange(v):
        t = raw_input().split()
        x = int(t[1])
        y = int(t[2])
        mat1[x-1][y-1] = t[0]
        mat2[x-1][y-1] = t[0]
        if t[0] == '+':
            diag[x-y] = 1
            adiag[x+y-2] = 1
            ans += 1
        elif t[0] == 'x':
            row[x-1] = 1
            col[y-1] = 1
            ans += 1
        else:
            diag[x-y] = 1
            adiag[x+y-2] = 1
            row[x-1] = 1
            col[y-1] = 1
            ans += 2

    for j in xrange(u):
        for k in xrange(u):
            if row[j] + col[k] == 0:
                ans += 1
                if mat1[j][k] == '.':
                    mat2[j][k] = 'x'
                else:
                    mat2[j][k] = 'o'
                row[j] = 1
                col[k] = 1

    k = 0
    for j in xrange(u):
        g = k - j
        h = k + j
        if diag[g] + adiag[h] == 0:
            diag[g] = 1
            adiag[h] = 1
            ans += 1
            if mat2[k][j] == '.':
                mat2[k][j] = '+'
            else:
                mat2[k][j] = 'o'

    k = u - 1
    for j in xrange(1, u - 1):
        g = k - j 
        h = k + j
        if diag[g] + adiag[h] == 0:
            diag[g] = 1
            adiag[h] = 1
            ans += 1
            if mat2[k][j] == '.':
                mat2[k][j] = '+'
            else:
                mat2[k][j] = 'o'
    
    model = []
    for k in xrange(u):
        for j in xrange(u):
            if mat2[k][j] != mat1[k][j]:
                model.append([k, j])
    
    print 'Case #' + str(i+1) + ': ' + str(ans) + ' '  + str(len(model))
    for k in model:
        print mat2[k[0]][k[1]], k[0] + 1, k[1] + 1




                
 
