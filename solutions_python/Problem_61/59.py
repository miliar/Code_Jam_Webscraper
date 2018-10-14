import sys
import operator


def solve(v):
    global Current
    #print v,Current
    if v>Current:
        for i in range(v-Current):
            Calc()
    return sum(Count[v])%100003
def Calc():
    global Current
    #print 'Calc current' + str(Current)
    Current=Current+1
    Count.append( [0]*Current )
    Count[Current][1]=1
    for i in range(1,Current):
        for j in range(i):
            #print "On ", Current, i,j,Count[Current-1],Count[Current]
            Count[Current][i]=Count[Current][i]+ Count[i][j]*NSelectK(Current-i-1, i-j-1)
            #print "On ", Current, i,j,Count[Current-1],Count[Current]
    
    
def NSelectK(N,k):
    if k>N:
        return 0
    if k>N/2:
        k=N-k
    if k==0:
        return 1
    prod=1
    for i in range(k):
        prod *= N-i
    for i in range(1,k+1):
        prod /= i
    return prod



if __name__== '__main__':
    a=[0]*3
    a[1]=2
    Count=[]
    Current=2
    Count.append([])
    Count.append([0])
    Count.append([0,1])
    
    cases=  int( sys.stdin.readline())
    for i in range(cases):
        v=[ int(item) for item in sys.stdin.readline().split() ]
        print 'Case #%d: %d'%(i+1,solve(v[0]))
