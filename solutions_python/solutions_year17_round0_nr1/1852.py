
def calc(cakes,k):
    sz = len(cakes)
    ans = 0
    for i in range(sz-1, k-2, -1):
        if not cakes[i]:
            ans +=1
            j = 0
            while j<k:
                cakes[i-j] = not cakes[i-j]
                j +=1
    if False in cakes:
        return "IMPOSSIBLE"
    else:
        return ans

for tt in range(input()):
    c,k = raw_input().strip().split()
    cakes = []
    for i in c:
        if i == '-':
            cakes.append(False)
        else:
            cakes.append(True)
    k = int(k)
    ans = calc(cakes,k)
    print "Case #{}: {}".format(tt + 1, ans)