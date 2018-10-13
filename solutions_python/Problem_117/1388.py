T = input()

for case in xrange(T):
    mat = []
    row, col = map(int, raw_input().split())
    for i in xrange(row):
        mat.append(map(int, raw_input().split()))
    if row == 1 or col == 1:
        print "Case #{0}: YES".format(case+1)
        continue
    
    while True:
        k = 0
        while k < len(mat):
            if not mat[k]:
                del mat[k]
                continue
            k += 1

        if not mat:
            break

        min = float('inf')
        minrow = 0
        mincol = 0
        for r in xrange(len(mat)):
            for c in xrange(len(mat[0])):
                    if min > mat[r][c]:
                        minr = r
                        minc = c
                        min = mat[r][c]

        numc = 0
        numr = 0
        rb = True
        cb = True

        for j in xrange(len(mat[minr])):
            if mat[minr][j] == min:
                numr += 1

        if numr != len(mat[minr]):
            rb = False

        for j in xrange(len(mat)):
            if mat[j][minc] == min:
                numc += 1

        if numc != len(mat):
            cb = False

        if cb == False and rb == False:
            print "Case #{0}: NO".format(case+1)
            break

        if cb:
            for j in xrange(len(mat)):
                del mat[j][minc]
        elif rb:
            del mat[minr]
    if len(mat) != 0:
        continue
    print "Case #{0}: YES".format(case+1)


