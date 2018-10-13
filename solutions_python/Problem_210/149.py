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


day = 60*24 # 1440
mm = 60 * 12 # 720

def dd(a,b): # forward distance
    while b<a:
        b+=day
    return b-a
    
def solve():
    #pprint("solve {}".format(s))
    c,j=map(int,input().split())
    cs=[]
    ce=[]
    js=[]
    je=[] 
    for i in range(c):
        s,e = map(int,input().split())
        cs.append(s)
        ce.append(e)
    for i in range(j):
        s,e = map(int,input().split())
        js.append(s)
        je.append(e)

    # small alg
    if len(cs)==1 or len(js)==1:
        print("2")
        return
    assert(len(cs)==2 or len(js)==2)
    if (len(cs)==2):
        ts=cs
        te=ce
    else:
        ts=js
        te=je
    for i in range(2):
        if dd(ts[i],te[1-i]) <= mm:
            print("2")
            return
    print("4")
    return


M()
    
