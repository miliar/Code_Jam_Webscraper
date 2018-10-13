import sys

def func(m,n):
    mbin=str(m)
    #nbin=str(n)
    mlen=len(mbin)
    #nlen=len(nbin)
    for i in range(0,mlen):
        mtem=mbin[mlen-i:]+mbin[:mlen-i]
        mint=int(mtem,10)
        if mint==n:
            return True
    return False

def count(m,n):
    c=0
    for i in xrange(m,n+1):
        for j in xrange(m,n+1):
            if i!=j:
                if func(i,j):
                    c=c+1
    return c/2

inname = "C-small-attempt0.in"
outname = "C-small-attempt0.out"
if len(sys.argv)>1:
    inname = sys.argv[1]
    outname = inname.rstrip(".in")
    outname = outname + ".out"

fin = open(inname,"r")
fout = open(outname,"w")
testCaseNum = int(fin.readline())
lines = fin.readlines()
caseNum = 0
for line in lines:
    caseNum = caseNum + 1
    line = line.rstrip('\n')
    answer = "Case #%d: " %(caseNum)
    [m_str,n_str]=line.split(' ')
    m=int(m_str)
    n=int(n_str)
    answer = answer + "%d"% count(m,n)
    answer = answer + "\n"
    fout.write(answer)

fin.close()
fout.close()