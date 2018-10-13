def longestEmpty(L) :
    maximal = 0
    left, right = 1,1
    for k in range (1, len(L)) :
        for i in range (k, len(L)) :
            if L[i] == 0 :
                left = i
                break
        for j in range (left, len(L)) :
            if L[j] == 1 :
                right = j-1
                break
        if j - i > maximal :
            maximal = j-i
            maxtup = left, right
    return maxtup
def getDistances(L, lastOne) :
    temp = lastOne - 1
    i = 0
    while(L[temp] == 0) :
        i += 1
        temp-=1
    temp = lastOne + 1
    j = 0
    while(L[temp] == 0):
        j += 1
        temp+=1
    return max(i, j), min(i, j)
        
T = int(input())

for i in range (0, T) :
    S = input().split()
    N = int(S[0])
    K = int(S[1])
    L = []
    L.append(1)
    for k in range (0, N):
        L.append(0)
    L.append(1)
    for j in range (0, K) :
        tup = longestEmpty(L)
        l, r = tup[0], tup[1]
        L[(l+r)//2] = 1
        lastOne = (l+r)//2
    result = getDistances(L, lastOne)
    print("Case #", i+1, ": ", result[0], " ", result[1], sep = "")
