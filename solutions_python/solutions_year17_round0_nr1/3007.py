
def solution(s,k):
    result=0
    t=[(0 if i=="-" else 1) for i in s]
    for i in list(range(len(s))):
        if t[i]==0:
            result+=1
            if (i+k)>len(s):
                return "IMPOSSIBLE"
            for j in list(range(i,i+k)):
                t[j]=1-t[j]
    return result
t = int(input())
for i in list(range(1, t + 1)):
    s,k=input().split(" ")
    k=int(k)
    print("Case #{}: {}".format(i, solution(s,k)))
