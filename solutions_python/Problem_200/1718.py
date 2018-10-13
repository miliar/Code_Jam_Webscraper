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
        print("".join([str(a) for a in solve(n)]))

def solve(i):
    S = input().strip()
    s = [x for x in map(int,list(S))]
    dprint("s=%s"%([x for x in s]))
    rev = False
    for i in range(len(s)-1):
        if s[i]>s[i+1]:
            rev = True
            break
    if not rev:
        return s
    while True:
        s[i]-=1
        if i==0 or s[i-1]<=s[i]:
            break
        i-=1
    for j in range(i+1,len(s)):
        s[j]=9
    if s[0]==0:
        s = s[1:]
    return s



if __name__ == "__main__":
    m()



