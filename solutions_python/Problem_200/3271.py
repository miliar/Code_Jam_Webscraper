
def solution(x):
    s=[int(i) for i in x]
    for i in list(range(len(s)-1,0,-1)):
        if s[i]<s[i-1]:
            s[i-1]-=1
            for x in list(range(i,len(s))):
                s[x]=9
    while s[0]==0:
        s=s[1:]
    result=""
    for t in s:
        result+=str(t)
    return result
t = int(input())
for i in list(range(1, t + 1)):
    x=input()
    print("Case #{}: {}".format(i, solution(x)))
