f = open("inp2", "rb")
t = int(f.readline())
for tt in range(1,t+1):
    n = int(f.readline())
    nn = n
    a = list()
    for i in range(n):
        b = map(int,f.readline().split())
        b.append(0)
        a.append(b)
    moves = 0
    stars = 0
    while nn > 0 :
        k = -1; ma = 0; mb = 0
        for i in range(n):
            if stars >= a[i][1] and a[i][2]<2:
                moves += 1
                stars += 2 - a[i][2]
                a[i][2] = 2
                nn -= 1
                k = 0
                break
        if k==0:
            continue
        for i in range(n):
            if stars >= a[i][0] and a[i][2]==0 and a[i][1]>mb:
                mb = a[i][1]
                k = i
        if k == -1:
            moves = "Too Bad"
            break
        a[k][2] = 1
        stars += 1
        moves += 1
    print "Case #{0}: {1}".format(tt,moves)
