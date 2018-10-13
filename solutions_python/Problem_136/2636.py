#import sys
eps = 0.000000001
n = int(input())
#sys.stdout = open('fff.txt','w')
for h in range(n):
    t = 2
    sm =  0
    sm1 = 2
    sm2 = 1
    c,f,x = map(float,input().split())
    while sm1  -  sm2 > eps:
        sm1 = sm + x / t
        sm += c / t
        t += f
        sm2 = sm + x / t
    print('Case #%d: %.7f' % (h + 1, min(sm1,sm2)))