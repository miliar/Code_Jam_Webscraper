def function(statusStr, K):
    statusList = list(statusStr)
    length = len(statusList)
    count = 0
    for i in range(length):
        if statusList[i] == '+':
            statusList[i] = 1
        else:
            statusList[i] = 0
    for i in range(length - K + 1):
        if statusList[i] == 0:
            count += 1
            for j in range(K):
                statusList[i+j] = 1 - statusList[i+j]
    for j in range(length - K + 1, length):
        if statusList[j] == 0:
            return "IMPOSSIBLE"
    return count

n = int(raw_input())
for i in range(n):
    input = raw_input().strip().split(' ')
    print "Case #{0}: {1}".format(i+1, function(input[0], int(input[1])))
