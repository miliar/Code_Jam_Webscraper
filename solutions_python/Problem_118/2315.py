from math import sqrt

def main():
    fi=open('C-small-attempt0.in','r')
    t=int(fi.readline())
    op=''
    for x in range(t):
        ip=fi.readline()
        ip=ip.split()
        up=int(ip[1])
        down=int(ip[0])
        co,s,p,rp=0,0,0,0
        for y in range(down,up+1):
            s=squ(y)
            if s==1:
                rp=pli(int(sqrt(y)))
                if rp==1:
                    p=pli(y)
                    if p==1:
                        co=co+1
        op=op+'Case #%d: %d\n'%(x+1,co)
    fo=open('outf.out','w')
    fo.write(op[:-1])
    fo.close()
    fi.close()

def pli(x):
    x=str(x)
    co=0
    if len(x)==1:
        return 1
    for y in range(len(x)/2):
        if x[y]==x[y-1]:
            co=co+1
        else:
            return 0
    if co==len(x)/2:
        return 1

def squ(x):
    if sqrt(x)-int(sqrt(x))==0.0:
        return 1
    else:
        return 0

if __name__=="__main__":
    main()
