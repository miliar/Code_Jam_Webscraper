import sys

dd=0
#dd=1

if dd:
    def dprint(*x):
        print("".join([str(a) for a in x]))
else:
    def dprint(*x):
        1


def m():
    N=int(input())
    for n in range(N):
        print("Case #%d: "%(n+1),end="")
        print(solve(n))

def flip(a):
    if a=="-":
        return "+"
    else:
        return "-"

def solve(i):
    S,K = input().strip().split()
    k = int(K)
    s = list(S)
    dprint("s=%s, k=%d"%(s,k))
    c=0
    for i in range(len(s)-k+1):
        if s[i]=="-":
            c+=1
            for j in range(k):
                s[i+j] = flip(s[i+j])
    for j in range(k-1):
        if s[-(j+1)] != "+":
            return "IMPOSSIBLE"
    return c

if __name__ == "__main__":
    m()



