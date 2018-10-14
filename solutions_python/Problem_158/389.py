fin = open('D-small-attempt0.in','r')
fout = open('D.out','w')
t=int(fin.readline())
INF=20000000000000000000

def res(x,r,c):
    if (r*c)%x != 0:
        return True
    if x==1:
        return False
    if x==2:
        return False 
    if x==3:
        return min(r,c)==1 or max(r,c)<3
    if x==4:
        r1=min(r,c)
        c1=max(r,c)
        if(c1<4):
            return True
        if(r1<3):
            return True
        return False
def ans(x,r,c):
    if res(x,r,c):
        return "RICHARD"
    else:
        return "GABRIEL"
for cas in xrange(1,t+1):
    x,r,c=map(int,fin.readline().split())
    fout.write("Case #{}: {}\n".format(cas,ans(x,r,c)))
fin.close()
fout.close()
