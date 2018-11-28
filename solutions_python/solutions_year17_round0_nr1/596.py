import time
##import sys
##sys.setrecursionlimit(10002)
INFILE='as.in'
OUTFILE='a.out'

rev=lambda x:'-' if x=='+' else '+'
def solve(s,k):
    bl=len([i for i in s if i=='-'])
    if bl==0:
        return 0
    if k==1:
        return bl
    for i in range(len(s)):
        if s[i]=='-':
            break
    for j in range(len(s)-1,i-1,-1):
        if s[j]=='-':
            break
    s=s[i:j+1]
##    print s
    if len(s)<k or (bl%2==1 and k%2==0):
        return 'IMPOSSIBLE'
    if s[:k]==['-']*k:
        ans0=solve(s[k:],k)
        return 'IMPOSSIBLE' if ans0=='IMPOSSIBLE' else ans0+1
    if s[-k:]==['-']*k:
        ans0=solve(s[:-k],k)
        return 'IMPOSSIBLE' if ans0=='IMPOSSIBLE' else ans0+1
    ans0=solve([rev(i) for i in s[:k]]+s[k:],k)
    ans1=solve(s[:-k]+[rev(i) for i in s[-k:]],k)
    if ans0==ans1=='IMPOSSIBLE':
        return 'IMPOSSIBLE'
    elif ans0=='IMPOSSIBLE':
        return ans1+1
    elif ans1=='IMPOSSIBLE':
        return ans0+1
    else:
        return min(ans0,ans1)+1
    return s,k

def read_input(fi):
    readInt=lambda type:type(fi.readline()[:-1])
    readArray=lambda type:map(type,fi.readline().split())
    readMatrix=lambda type,x:[map(type,fi.readline().split()) for i in range(x)]
    readLines=lambda type,x:[type(fi.readline()[:-1]) for i in range(x)]
    inp=readArray(str)
    s=list(inp[0])
    k=int(inp[1])
    return s,k

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