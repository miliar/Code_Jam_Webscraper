import sys
f = open("al.in")
def raw_input():
    return f.readline().strip()
d={'.':0,'^':2,'v':4,'<':3,'>':1}
def g(x):
    return d[x]
def h(a,x,y):
    if a==1:
        return (x+1,y)
    elif a==2:
        return (x,y-1)
    elif a==3:
        return (x-1,y)
    elif a==4:
        return (x,y+1)
sys.stdout=open("out",'w')
for i in range(int(raw_input())):
    print "Case #%d:"%(i+1),
    r,c= map(int, raw_input().split())
    l=[[] for i in range(r)]
    for i in range(r):
        l[i]=list(map(g, raw_input()))
    def v(x,y):
        return 0<=x<c and 0<=y<r
    def ch(t,x,y):
        x,y=h(t,x,y)
        while v(x,y) and not l[y][x]:
            x,y=h(t,x,y)
        return v(x,y)
    b= True
    ct=0
    for y in range(r):
        if not b:
            break
        for x in range(c):
            t=l[y][x]
            if l[y][x]:
                if not ch(t,x,y):
                    for i in range(3):
                        t=t%4+1
                        if ch(t,x,y):
                            ct+=1
                            break
                    else:
                        b=False
                        break
    print ct if b else "IMPOSSIBLE"
                    