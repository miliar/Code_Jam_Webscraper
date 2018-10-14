import sys

# 2017QR
# https://code.google.com/codejam/contest/3264486/dashboard

def A():
    #T=input()
    for t in range(input()):
    	S,K=raw_input().split()
        #print S,K
        K=int(K)
        S=[s=='+' for s in S]
        count=0
        for x in range(len(S)-K+1):
            if S[x]: continue
            count+=1
            for y in range(x,x+K):
                S[y]=not S[y]
        if all(S):
            print "Case #{}: {}".format(t+1,count)
        else:
            print "Case #{}: {}".format(t+1,'IMPOSSIBLE')

def B():
    def maxnum(n):
        return max(map(int,list(str(n))))
    def solve(n):
        if n<10: return n
        if maxnum(n//10)<=n%10:
            m=solve(n//10)
            if m==n//10:
                return m*10+n%10
            else:
                return m*10+9
        else:
            m=solve(n//10-1)
            return m*10+9
    for t in range(input()):
    	N=input()
        print "Case #{}: {}".format(t+1,solve(N))

def C():
    def solve(n,k):
        s=[n]
        while k:
            s.sort()
            r=s.pop()-1
            if r%2:
                s.append(r//2+1)
                s.append(r//2)
            else:
                s.append(r//2)
                s.append(r//2)
            k-=1
        return s[-2:]
    def solve2(N,K):
        #print "#", N,K
        if K==1: return [(N-1)//2+(N-1)%2, (N-1)//2]

        k=1
        while k<=K:
            k<<=1
        k>>=1

        N=N-k+1
        p=K-k
        #print "#", k,N,p

        A=N//k
        B=N%k
        C=A+1 if p<B else A
        #print "#", A,B,C
        C=C-1
        return [C//2+C%2,C//2]
    for t in range(input()):
    	N,K=map(int,raw_input().split())
        y,z=solve2(N,K)
        print "Case #{}: {} {}".format(t+1,y,z)

C()
