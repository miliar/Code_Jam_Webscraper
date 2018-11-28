
ifile = open("A-small-attempt0.in", 'r')
ofile = open("gcj-r-1CCs.txt", 'w')


T = int(ifile.readline())

for c in range(T):
    N = int(ifile.readline())
    paramLs = []
    for l in range(N):
        ys = map(float, ifile.readline().split())
        param = [ys[1] - ys[0], ys[0]]
        paramLs.append(param)

    pointLs = []
    for i in range(N):
        a1 = paramLs[i][0]
        b1 = paramLs[i][1]
        for j in range(i+1, N):
            a2 = paramLs[j][0]
            b2 = paramLs[j][1]
            
            if a1 == a2:
                continue
            x = (b1 - b2)/(-a1 + a2)
            y = (-a1*b2+a2*b1)/(-a1+a2)
            
            if [x, y] in pointLs or (0 >= x or x >= 1):
                continue
            else:
                point = [x, y]
                pointLs.append(point)
    ofile.write("Case #%d: %d\n" % (c+1, len(pointLs)))
                
                