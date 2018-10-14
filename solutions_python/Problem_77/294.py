maxn = 1001
res = [0]*maxn
'''
eps = 0.00000000001
D = [[0 for j in range(maxn)]for i in range(maxn)]
D[0][0] = 1.0
D[1][0] = 0.0
D[1][1] = 1.0
for i in range(2,maxn):
    D[i][0] = ((i-1)*D[i-1][0]+D[i-2][0])/i
    for j in range(1,i+1):
        D[i][j] = D[i-j][0]
        for k in range(1,j+1):
            D[i][j]/=k
            if D[i][j]<eps:
                D[i][j] = 0.0
                break
#print D
res[0] = 0.0
res[1] = 0.0
for i in range(2,maxn):
    p = D[i][0]
    s = 1.0
    for j in range(i):
        s+=res[i-j]*D[i][j]
    res[i] = s/(1-p)
print res
'''
for i in range(2,maxn):
    res[i] = i*1.0
fi = open("input.txt")
T = int(fi.readline())
for test in range(T):
    n = int(fi.readline())
    a = map(int,fi.readline().split())
    assert n == len(a)
    x = n
    for i in range(n):
        a[i]-=1
        if i==a[i]:
            x-=1
    print "Case #{0}: {1}".format(test+1,res[x])
fi.close()
