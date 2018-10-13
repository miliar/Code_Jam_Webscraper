def good(numberStr):
    numberList = map(int, list(numberStr))
    length = len(numberList)
    notYetFix = 0
    for i in range(length - 1):
        if numberList[i] < numberList[i+1]:
            notYetFix = i+1
        elif numberList[i] > numberList[i+1]:
            break
        elif i == length - 2 and numberList[i] == numberList[i+1]:
            notYetFix = length - 1
    if notYetFix != length - 1:
        numberList[notYetFix] -= 1
        for j in range(notYetFix+1, length):
            numberList[j] = 9
    resultList = map(str, numberList)
    if resultList[0] == '0':
        resultList[0] = ''
    return ''.join(resultList)

n = int(raw_input())
for i in range(n):
    input = raw_input().strip()
    print "Case #{0}: {1}".format(i+1, good(input))
