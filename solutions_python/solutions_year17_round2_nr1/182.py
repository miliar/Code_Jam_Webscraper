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
    d,n=map(int,input().split())
    latest = -1.0
    for i in range(n):
        k,v = map(int,input().split())
        arr = (d-k)/v
        if arr>latest:
            latest=arr
    vv = d/latest
    print(vv)


def cl(line):
    return sum([1 if x!="?" else 0 for x in line])

def sline(line):
    for c in line:
        if c != "?":
            break
    for i in range(len(line)):
        if line[i]=="?":
            line[i]=c
        elif line[i]!="c":
            c=line[i]


def scake(cake):
    l=0
    while(cl(cake[l])==0):
        l+=1

    pprint("first nonempty %d"%l)
    sline(cake[l])
    for i in range(l):
        cake[i]=cake[l]
        pprint("%d from %d"%(i,l))

    while True:
        m = l+1
        while(m<len(cake) and cl(cake[m])==0):
            m+=1
        if m==len(cake):
            for i in range(l+1,m):
                pprint("%d,%d,%s,%s"%(i,l,cake[i],cake[l]))
                cake[i] = cake[l]
                pprint("%d,%d,%s,%s"%(i,l,cake[i],cake[l]))
                pprint(". %d from %d"%(i,l))
            break
        sline(cake[m])
        for i in range(l+1,m):
            cake[i]=cake[l]
            pprint(".. %d from %d"%(i,l))
        l=m

    for i in range(len(cake)):
        print("".join(cake[i]))
    


M()
    
