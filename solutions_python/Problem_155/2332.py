from sys import argv

def getMinFriendCount(n, s):
    standingAudienceCount = s[0]
    friendsNeeded = 0
    if standingAudienceCount == 0:
        friendsNeeded += 1
        standingAudienceCount += 1
    for i in range(1,N+1):
        if standingAudienceCount >= i:
            standingAudienceCount += s[i]
        else:
            friendsNeededAtS =  i - standingAudienceCount
            standingAudienceCount += friendsNeededAtS + s[i]
            friendsNeeded += friendsNeededAtS
    return friendsNeeded

script, inputFile = argv
inputData = open(inputFile, 'r')
T = int(inputData.readline())
counter = 0
while T:
    N, A = inputData.readline().split()
    N = int(N)
    S = map(int, list(A))
    counter += 1
    ans = getMinFriendCount(N, S)
    ansStr = "Case #%d: %d" %(counter, ans)
    print ansStr
    T -= 1
