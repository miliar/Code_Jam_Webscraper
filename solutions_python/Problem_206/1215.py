from __future__ import division
T=int(input())
for q in range(1,T+1):
    a=map(int,raw_input().strip().split(' '))
    d=a[0]
    n=a[1]
    horse={}
    h=[]
    for i in range(n):
        b=map(int,raw_input().strip().split(' '))
        horse[b[0]]=b[1]
        h.append(b[0])
    h.sort()
    h.reverse()
    t=[]
    for i in h:
        t.append((d-i)/horse[i])
    ans=(d/(max(t)))
    print "Case #{}:".format(q),format(ans,'.6f')
