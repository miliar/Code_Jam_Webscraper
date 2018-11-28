from scipy.optimize import linear_sum_assignment as hung

Cases = int(input())
for Case in range(Cases):
    n, c, m = map(int,input().split())
    k = [[] for _ in range(c)]
    ones = [0]*c
    for i in range(m):
        p, b = map(int,input().split())
        k[b-1].append(p)
        if p == 1:
            ones[b-1] += 1
    
    for l in k:
        l.sort()

    a,b = k[0],k[1]
    if len(a) > len(b):
        a,b = b,a

    y = max(len(a),len(b))
    z = 0

    # print(a,b)

    if len(a)*len(b) > 0:
        M = [[0] * len(b) for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    M[i][j] = 1
                    if a[i] == 1:
                        M[i][j] = 10000
        for aa,bb in zip(*hung(M)):
            if M[aa][bb] != 10000:
                z += M[aa][bb]
            else:
                y += 1
    print('Case #%d: %d %d' % (Case+1, y, z))
