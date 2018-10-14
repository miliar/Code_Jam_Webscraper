import sys

def slove():
    icase = int(input())
    for i in range(icase):
        c = int(input())
        cs = [int(j) for j in input().split()]
        a = 0
        for k in cs:
            a = a^k
        if a != 0:
            print('Case #%d: NO'%(i+1))
        else:
            print('Case #%d:'%(i+1), sum(cs)-min(cs))


slove()        