
def isTidy(s):
    for i in range(len(s)-1):
        if (s[i] > s[i+1]):
            return False

    return True

def returnTidy(s):
    sLen = len(s)
    indexToDecrease = 0

    for i in range(sLen-1):
        if (s[sLen - 2 - i] > s[sLen - 1 - i]):
            indexToDecrease = sLen - i - 2
            break

    s[indexToDecrease] = str( int(s[indexToDecrease]) - 1 )
    for i in range(indexToDecrease + 1, sLen):
        s[i] = "9"

    return s

def stripZeros(s):
    while(True):
        if (s[0] == "0"):
            del s[0]
        else:
            return s


#s = list("3215")
#s = returnTidy(s)
#
#s = stripZeros(s)
#print(s)

T = int(input())
case = 0

try:
    while True:
        line = input()
        case += 1
        s = list(line)

        while (not isTidy(s)):
            s = returnTidy(s)

        s = stripZeros(s)

        s = ''.join(s)

        print('Case #{}: {}'.format(case, s))

except EOFError:
    pass
