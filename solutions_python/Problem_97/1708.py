from math import log10

def read1():
    with open('in') as f:
        s = f.readlines()
        T = int(s[0].strip())
        return [tuple(map(int,x.strip().split(' '))) for x in s[1:] ]
    
def solve(A,B):
    ss=set()
    D = len(str(A))
    for i in range(A,B+1):
        orig=i
        s = str(i)*2
        for j in range(D):
            x = int(s[j:j+D])
            if x > orig and A <= x and x <= B :
                ss.add( (i,x) )
    return len(ss)

out = open('out','w')
for i, (a,b) in enumerate(read1()):
    ss = 'Case #%d: %s'%(1+i,solve(a,b))
    print ss
    print >> out , ss
