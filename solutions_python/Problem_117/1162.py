t = int(input())
for i in range(1, t+1):
    lawn = []
    psbl = 1
    (n, m) = tuple(int(c) for c in input().split())
    for j in range(0, n):
        lawn.append(list(int(c) for c in input().split()))
    for j in range(0, n):
        for k in range(0, m):
            if max(lawn[j]) > lawn[j][k] and max(lawn[c][k] for c in range(0, n)) > lawn[j][k]:
                psbl = 0
                break
##            if ((k>0 and lawn[j][k-1]>lawn[j][k]) or (k<m-1 and lawn[j][k]<lawn[j][k+1]))\
##               and ((j>0 and lawn[j-1][k]>lawn[j][k]) or (j<n-1 and lawn[j][k]<lawn[j+1][k])):
##                psbl = 0
##                break
##            if (lawn[j][k-1] > lawn[j][k] < lawn[j][k+1] or (k==0 and lawn[j][k] < lawn[j][k+1]) or (k==m-1 and lawn[j][k-1] > lawn[j][k]))\
##               and (lawn[j-1][k] > lawn[j][k] < lawn[j+i][k] or (j==0 and lawn[j][k] < lawn[j+1][k]) or (j==n-1 and lawn[j-1][k] > lawn[j][k])):
##                psbl = 0
##                break
        if psbl == 0:
            break
    print('Case #%i: %s' % (i, ['NO', 'YES'][psbl]))
