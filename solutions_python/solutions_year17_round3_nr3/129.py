#!/usr/bin/python3

pp=0
#pp=1


if (pp):
    def pprint(*ll):
        print("".join(map(str,list(ll))))
else:
    def pprint(*ll):
        1


def M():
    t = int(input())
    for i in range(1, t + 1):
        print("Case #%d: "%i,end="")
        solve()


def solve():
    #pprint("solve {}".format(s))
    n,k=map(int,input().split())
    u=float(input())
    pprint("n=%d, k=%d, u=%f"%(n,k,u))
    p=sorted(list(map(float,input().split())))
    pprint(p)

    # small alg
    for i in range(1,n): # check
        # p[j] equal up to p[i-1], u remains to assign
        # can we bring p..i beyond p[i+1]?
        ud = u/(i)
        if p[i-1] + ud < p[i]:
            for j in range(i):
                p[j]+=ud
            # all u assigned
            u = -1
            break
        # else bring all up to p[i], deduct from u
        u -= i*(p[i]-p[i-1])
        for j in range(i):
            p[j]=p[i]
    pprint(p)
    if u>0:
        ud = u/n
        pprint("supp")
        for i in range(n):
            p[i] += ud
    pprint(p)
    ppp=1.0
    for i in range(n):
        ppp *= p[i]
    print(ppp)

    
    


M()
    
