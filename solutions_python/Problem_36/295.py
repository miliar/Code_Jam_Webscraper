import sys

s=r'welcome to code jam'
def func(s_,inp_,m,n):
    ls=len(s_)
    li=len(inp_)
    if(ls==0 ):
        return 1
    if(ls>li):
        return 0
    if(metrics[m][n]>=0):
        return metrics[m][n]
    res=0
    i=0
    while(i < (li-ls+1)):
        if(s_[0] == inp_[i]):
            res += func(s_[1:],inp_[i+1:],m+i+1,n+1) %10000
        i += 1
    metrics[m][n]=res
    return res
inps=open(sys.argv[1],"r").readlines()
length=inps[0]
k=1
for inp in inps[1:]:
    metrics=[[-1 for j in range(0,len(s))] for i in range(0,len(inp))]
    result=func(s,inp,0,0) % 10000
    rr = "Case #%d: %04d" % (k, result)
    print rr
    if k >= length: break
    k += 1
