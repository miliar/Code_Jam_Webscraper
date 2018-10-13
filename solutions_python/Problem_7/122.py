import sys


fin = open(sys.argv[1])

fout = open(sys.argv[2], 'w')
#fout = sys.stdout

N = int(fin.readline())

for t in range(N):
    # generate all points and put in set (unique list)
    points = set()
    n, A, B, C, D, x0, y0, M = [int(x) for x in fin.readline().split()]
    #print "input", n, A, B, C, D, x0, y0, M 
    
    X = x0
    Y = y0
    points.add((X, Y))
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        points.add((X, Y))

    #print points
    
    points2 = []
    for a in points:
        points2.append(a)
    
    # iterate through unique triplets
    count = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if ((points2[i][0]+points2[j][0]+points2[k][0])%3 == 0 and (points2[i][1]+points2[j][1]+points2[k][1])%3 == 0):
                    count += 1
    print >>fout, "Case #%d: %d" %(t+1,count)
    