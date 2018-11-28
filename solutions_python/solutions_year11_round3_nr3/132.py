def gcd(x,y):
    if (y==0):
        return x
    else:
        return gcd(y, x%y)

def readIntList():
    return [int(k) for k in input().split()]

caseNum = int(input())
for caseId in range(1, caseNum+1):
    playerNum, low, high = readIntList()
    playerList = readIntList()[0:playerNum]

    ans=-1
    for i in range(low, high+1):
        ok=True
        for player in playerList:
            if (i%player==0 or player%i==0):
                continue
            else:
                ok=False
                break
        if (ok):
            ans=i
            break

    if (ans==-1):
        print("Case #%d: NO" % (caseId), end="\n")
    else:
        print("Case #%d: %d" % (caseId, ans), end="\n")


