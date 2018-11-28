def findFirstOccurrence(num):
    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i+1]):
            return i
    return -1

def maxTidy(N):
    num = str(int(N)) # remove trailing 0s
    first = findFirstOccurrence(num)
    if first < 0:
        return num
    else:
        newNum = num[:first] + str(int(num[first]) - 1)
        for i in range(len(num[first+1:])):
            newNum += '9'
        return maxTidy(newNum)

t = int(input())
for i in range(1, t + 1):
    inp = input()
    print('Case #{}: {}'.format(i, maxTidy(inp)))
