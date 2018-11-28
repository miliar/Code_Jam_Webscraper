
import sys
sys.stdin=open("data.txt")
sys.stdout=open("out.txt","w")
input=sys.stdin.readline

t=int(input())

for cnum in range(t):
    s,s2=input().split()
    arr=[0 if ch=='+' else 1 for ch in s]
    k=int(s2)
    ans=0
    for i in range(k-1,len(arr))[::-1]:
        if arr[i]:
            # flip the range [i-k+1,i]
            for j in range(i-k+1,i+1):
                arr[j]=1-arr[j]
            ans+=1
    if sum(arr): print("Case #%d: IMPOSSIBLE"%(cnum+1))
    else: print("Case #%d: %d"%(cnum+1,ans))

