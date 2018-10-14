import math

def isPalindromes(num):
    strNum = str(num)
    lenNum = len(strNum)
    if lenNum == 1:
        return True
    for i in range(lenNum):
        if strNum[i] != strNum[lenNum - i - 1]:
            return False
    return True

def proc(A, B):
    count = 0
    sqA = int(math.sqrt(A))
    sqB = int(math.sqrt(B))
    #    print A, B, sqA, sqB
    for i in range(sqA, sqB + 1):
        k = i * i
        if A <= k and k <= B:
            if isPalindromes(k) and isPalindromes(i):
                #                print k, i
                count += 1
    return count

CaseNum = 0
i = 0
for line in open('C-small-attempt0.in', 'r'):
    #for line in open('input.txt', 'r'):
    if i == 0:
        CaseNum = int(line)
        i += 1
        continue

    d = map(int, line.split(' '))
    result = proc(d[0], d[1])
    print "Case #" + str(i) + ": " + str(result)
    i += 1
