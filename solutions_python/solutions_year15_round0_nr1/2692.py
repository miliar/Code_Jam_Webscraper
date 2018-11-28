__author__ = 'johnnydew'

def inviteMoreFriends(maxShy, audience):
    # print 'maxShy %s, audience %s' % (maxShy, audience)
    audienceCount = int(audience[0])
    needMoreCount = 0
    for i in range(1, maxShy+1):
        if (int(audience[i] > 0) and i > audienceCount):
            diff = i - audienceCount
            audienceCount = audienceCount + diff
            needMoreCount = needMoreCount + diff
        audienceCount = audienceCount + int(audience[i])
    return needMoreCount

if __name__ == '__main__':
    fIn = open('A-large.in', 'r')
    fOut = open('A-large.out', 'w')
    caseCount = int(fIn.readline())
    # print 'caseCount: %s' % (caseCount)
    for i in range(caseCount):
        caseParams = fIn.readline().split()
        moreFriendsCount = inviteMoreFriends(int(caseParams[0]), caseParams[1])
        resultStr = 'Case #%d: %d' % (i+1, moreFriendsCount)
        fOut.writelines(resultStr)
        fOut.writelines("\n")
    fIn.close()
    fOut.close()