import time
##import sys
##sys.setrecursionlimit(10002)
INFILE='bl.in'
OUTFILE='b.out'

def solve(n):
    l=map(int,[i for i in list(str(n))])
    sl=len(l)
    for i in range(sl-2,-1,-1):
        if l[i]>l[i+1]:
            l[i]-=1
            l[i+1:]=[9]*(sl-i-1)
    if l[0]==0:
        l=l[1:]
    return ''.join(map(str,l))

def read_input(fi):
    read=lambda type:type(fi.readline()[:-1])
    readArray=lambda type:map(type,fi.readline().split())
    readMatrix=lambda type,x:[map(type,fi.readline().split()) for i in range(x)]
    readLines=lambda type,x:[type(fi.readline()[:-1]) for i in range(x)]
    n=read(int)
    return (n,)

def main():
    fi=file(INFILE)
    fo=file(OUTFILE,'w')
    time0=time.time()
    t=int(fi.readline())
    for ti in range(t):
        time1=time.time()
        ans="Case #%d: %s"%(ti+1,solve(*read_input(fi)))
        print ans,"%.3f"%(time.time()-time1)
        fo.write(ans+'\n')
    print "%.3f"%(time.time()-time0)
    fi.close()
    fo.close()

if __name__ == '__main__':
    main()