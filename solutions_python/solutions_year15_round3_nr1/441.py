from math import ceil
t=int(raw_input())
for case in range(t):
    r,c,w=map(int,raw_input().split())
    c=int(ceil(((c*1.0)/w))+w-1)
    print "Case #{}: {}".format(case+1,c)
