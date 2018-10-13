import sys

def proc_case():
    n_es=int(sys.stdin.readline())
    v0=map(int,sys.stdin.readline().split())
    v1=map(int,sys.stdin.readline().split())
    
    v0.sort()
    v1.sort()
    
    prod=0
    for (x0,x1) in zip(v0,list(reversed(v1))):
        prod+=x0*x1
    
    return '%d'%prod

def proc_all():
    n_case=int(sys.stdin.readline().rstrip())
    for i in range(n_case):
        print 'Case #%d: %s'%(i+1,proc_case())
    

proc_all()
    

