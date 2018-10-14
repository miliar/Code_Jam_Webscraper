
def toHappyPancakes(s,k):
    if len(s)==0:
        return 0
    if len(s)<k:
        for j in range(len(s)):
            if not s[j]:
                return "IMPOSSIBLE"
    elif len(s)==k:
        sideU = 0
        sideD = 0
        for j in range(len(s)):
            if not s[j]:
                sideD+=1
            else:
                sideU+=1
        if sideU>0 and sideD>0:
            return "IMPOSSIBLE"
        if sideU>0:
            return 0
        return 1
    else:
        if s[0]:
            return toHappyPancakes(s[1:],k)
        else:
            s1 = s[1:]
            for j in range(k-1):
                s1[j]=0 if s1[j] else 1
            p1 = toHappyPancakes(s1,k)
            if type(p1)==str:
                return p1
            else:
                return p1+1

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    S = input().split()
    K = int(S[1])
    S = [0 if x=='-' else 1 for x in S[0]]
    print("Case #{}: {}".format(i, toHappyPancakes(S,K)))
    # check out .format's specification for more formatting options
