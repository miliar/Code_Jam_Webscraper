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

def most(r):
    if r[0]>r[1]:
        if r[0]>r[2]:
            return 0
        else:
            return 2
    if r[1]>r[2]:
        return 1
    else:
        return 2

#def ordy(r):
#    return sorted(range(3), key = lambda x: -r[x])

def ord2(r):
    assert(len(r)==3) # derived rem R' Y' B'
    if r[0]>r[1]:
        if r[1]>r[2]:
            return [1,5,0,3,2,4]
        else:
            if r[0]>r[2]:
                return [5,1,0,3,4,2]
            return [5,3,4,1,0,2]
    else:
        if r[2]>r[1]:
            return [3,5,4,1,2,0]
        else:
            if r[0]>r[2]:
                return [1,3,2,5,0,4]
            else:
                return [3,1,2,5,4,0]
            

def dr(r):
    return [r[0]+r[1]+r[5],r[1]+r[2]+r[3],r[3]+r[4]+r[5]]

def clash(x,y):
    if x=="R":
        return y == "R" or y== "O" or y=="V"
    if x=="Y":
        return y == "Y" or y== "O" or y=="G"
    if x=="B":
        return y == "B" or y== "G" or y=="V"
    if x=="O":
        return y != "B"
    if x=="G":
        return y != "R"
    if x=="V":
        return y != "Y"

def solve():
    # R O  Y G  B V
    # R,RY,Y,BY,B,RB                
    N,R,O,Y,G,B,V = map(int,input().split())
    a=[]
    # small, only R,Y,B
    rem = [R,O,Y,G,B,V]
    c = ["R","O","Y","G","B","V"]
    n = R+O+Y+G+B+V
    assert(n==N)
    drem = dr(rem) # [R',Y',B']
    mo = ord2(drem)
    ok=False
    for i in range(6):
        mi = mo[i]
        #if clash(c[mi],a[-1]):
        #                continue
        if rem[mi]<1:
            continue
        ok = True
        break
    assert(ok)
    pprint("> ",mo,mi,rem,drem)
    a.append(c[mi])
    rem[mi] -= 0.5
    # dec rem[most] but add one for loop...
    while len(a)<n:
        drem = dr(rem)
        mo = ord2(drem)
        ok=False
        for i in range(6):
            mi = mo[i]
            if clash(c[mi],a[-1]):
                continue
            if rem[mi]<1:
                continue
            ok = True
            break
        pprint(mo,mi,rem,drem)
        if not ok:
            print("IMPOSSIBLE")
            return
        #assert(rem[mi]>=0)
        a.append(c[mi])
        rem[mi] -= 1
    if clash(a[0],a[-1]):
        print("IMPOSSIBLE")
    else:
        print("".join(a))
    return

    
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
    
