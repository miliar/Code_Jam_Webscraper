import time
##import sys
##sys.setrecursionlimit(10002)
INFILE='al.in'
OUTFILE='a.out'

def solve(d,n,nx):
    kx=[(d-i[0]) for i in nx]
    sx=[i[1] for i in nx]
    tx=[1.0*kx[i]/sx[i] for i in range(n)]
    t=max(tx)
    ans=d/t

    return ans

def read_input(fi):
    read=lambda type:type(fi.readline()[:-1])
    readArray=lambda type:map(type,fi.readline().split())
    readMatrix=lambda type,x:[map(type,fi.readline().split()) for i in range(x)]
    readLines=lambda type,x:[type(fi.readline()[:-1]) for i in range(x)]
    d,n=readArray(int)
    nx=readMatrix(int,n)
    return d,n,nx

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
