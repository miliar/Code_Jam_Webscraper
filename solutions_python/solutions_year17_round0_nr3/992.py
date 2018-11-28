from math import sqrt, floor, ceil, log

def solve():
    N,K = [int(i) for i in input().split()]

    s = (ceil((N-1)/2), floor((N-1)/2))
    if(K==1): return "%d %d" % (max(s), min(s))

    c = floor(log(K)/log(2))
    b = "{0:b}".format(K)[-c:][::-1]

    for i in b:
        t = max(s[int(i)]-1,0)/2
        s = (ceil(t), floor(t))

    for i in range(0,len(b)-c):
        t = max(s[0]-1,0)/2
        s = (ceil(t), floor(t))

    return "%d %d" % (max(s), min(s))


T=int(input())
for t in range(1,T+1):
    print("Case #%d: %s" % (t, solve()))
