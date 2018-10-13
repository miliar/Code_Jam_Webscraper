__author__ = 'rainp1ng'

def main(inr,outr):
    t=int(inr.readline())
    for i in range(t):
        outr.write("Case #%s: "%(i+1)+solve(inr)+"\n")

def solve(inr):
    l=map(int,inr.readline().split())
    x=l[0]
    r=l[1]
    c=l[2]
    if r<x and c<x:
        return "RICHARD"
    cells=r*c
    if cells%x!=0:
        return "RICHARD"
    width=x/2+x%2
    print "x:",x,":",width
    if width>r or width>c:
        return "RICHARD"
    if x==4:
        if r==2 or c==2:
            return "RICHARD"
        else:
            return "GABRIEL"
    else:
        return "GABRIEL"


inr=open("/Users/rainp1ng/Downloads/Contest/GoogleCodeJam/identification_round/D-small-attempt3.in","rb")
outr=open("/Users/rainp1ng/Downloads/Contest/GoogleCodeJam/identification_round/output","wb")

main(inr,outr)

