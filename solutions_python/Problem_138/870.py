def war(n,k,N):
        k = sorted(k)
        n = sorted(n)
        i,j=0,0
        score=N
        while True:
                if (i > N-1 or j > N-1): break
                while True:
                        if (i > N-1 or j > N-1): break
                        if (k[j]<n[i]):
                                j+=1
                                if (j > N-1): break
                        else:
                                score-=1
                                i+=1
                                j+=1
        return score

def cheat(n,k,N):
        k = sorted(k)
        n = sorted(n)
        i,j=0,0
        r=N-1
        score=0
        while True:
                if (i>N-1 or j>N-1 or r<0): break
                while True:
                        if (i > N-1 or j > N-1): break
                        if (n[i]<k[j]):
                                k[r]=0
                                i+=1
                                r-=1
                        else:
                                score+=1
                                i+=1
                                j+=1
        return score
                
T = int(raw_input())
for case in range(1, T + 1):
        N = int(raw_input())
        n = map(float,raw_input().split())
        k = map(float,raw_input().split())
        print "Case #%d: " % (case), cheat(n,k,N), war(n,k,N)
