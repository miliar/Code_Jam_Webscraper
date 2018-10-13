import sys

def solve(D,N,KS):

    tmax=-1
    for i in range(N-1,-1,-1):
        t=float(D-KS[i][0]) / KS[i][1]
        #print(t)
        if (t>tmax):
            tmax=t

    return D/tmax

if __name__=='__main__':

    T = int(sys.stdin.readline())
    for i in range(T):
        (D,N) = (int(x) for x in sys.stdin.readline().rstrip().split())
        KS=[]
        for j in range(N):
            (k,s) = (int(x) for x in sys.stdin.readline().rstrip().split())
            KS.append((k,s))

            KS.sort()

        y = solve(D,N,KS)

        print("Case #%d: %.6f" % (i+1, y))
