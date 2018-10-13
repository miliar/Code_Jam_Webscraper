import sys

def rotate(str, n):
    return str[n:]+str[:n]


def are_recycled(n1,n2):
    s1=str(n1)
    s2=str(n2)
    if(len(s1)!=len(s2)):
        return false;
    
    for i in range(len(s1)-1):
        _s1=rotate(s1,i+1)
        if(int(_s1)==n2):
            return True
    return False


def num_recycled(fro, to):
    num=0
    for i in range(fro,to+1):
        for j in range(i,to+1):
            if i!=j and are_recycled(i,j):
                num=num+1
    return num


nlines=int(sys.stdin.readline())
i=0
for line in sys.stdin:
    i=i+1
    vals=map(int,line.strip().split())
    n=num_recycled(vals[0],vals[1])
    print 'Case #%(i)d: %(n)d' % {'i':i, 'n':n}
