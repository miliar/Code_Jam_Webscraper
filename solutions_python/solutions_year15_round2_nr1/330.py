def doit():
    n = int(raw_input())
    L = []
    for i in range(0, n+1):
        L.append(10000000)
    L[1] = 1
    curr = 1
    for i in range(1, n):
        curr = min(curr, L[i])
        flip = int(str(i)[::-1])
        if(flip > curr and flip <= n):
            L[flip] = min(curr+1, L[flip])
        L[i+1] = min(curr+1, L[i+1])
        curr += 1

    return L[n]


T = int(raw_input())
for i in range(1, T+1):
    print "Case #" + str(i) + ": " + str(doit())
        
