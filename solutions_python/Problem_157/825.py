def mult(a,b):
    global mat
    r = mat[abs(a)-1][abs(b)-1]
    if(a*b<0): return -r
    return r

def rec(d,i,f,r):
    global S
    global dp
    if(dp[d][i]==-1):
        return "NO"

    while(f!=len(S)):
        if(r==d and d<4):
            ret = rec(d+1,f,f+1,S[f])
            if(ret=="YES"): return "YES"
        r = mult(r,S[f])
        f = f+1
    
    if(f==len(S) and d==r and d==4):
        return "YES"
    dp[d][i]=-1
    return "NO"

def solve():
    global S,dp
    L,X = [int(i) for i in input().split()]
    dp = {2: [0]*(L*X), 3:[0]*(L*X), 4:[0]*(L*X)}
    S = input()*X
    S = [i for i in S]
    for k in range(0,len(S)):
        if(S[k]=='i'):
            S[k]=2
        elif(S[k]=='j'):
            S[k]=3
        elif(S[k]=='k'):
            S[k]=4
   
    return rec(2,0,1,S[0])

if __name__ == '__main__':
    # 1=1, i=2, j=3, k=4
    global mat 
    mat = [[1,2,3,4],[2,-1,4,-3],[3,-4,-1,2],[4,3,-2,-1]]

    T = int(input())

    for t in range(1,T+1):
        print("Case #%d: %s" % (t,solve()))
