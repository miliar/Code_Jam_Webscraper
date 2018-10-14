import sys, os, operator



def maxes(tot):
    med = tot / 3
    mod = tot % 3
    if tot == 0:
        return (0,0)
    if mod == 0:
        return (med, med+1)
    if mod == 1:
        return (med +1 , med +1)
    if mod == 2:
        return (med+1, med+2)



#f = open("sample-in.txt")
f = sys.stdin

cases = f.readline()
for case in xrange(1,int(cases)+1):
    inputs = map(int,f.readline().split())
    n,s,p = inputs[:3]
    scores = inputs[3:]
    goods = 0
    for score in scores:
        if maxes(score)[0] >= p:
            goods+=1
        elif maxes(score)[1] == p and s>0:
            goods+=1
            s-=1

    print 'Case #%d: %d'%(case,goods)

  