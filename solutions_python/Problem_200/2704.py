def findFirstDecreasingPointOf (num: str):
    last = num[0]
    for i, c in enumerate(num[1:]):
        if last > c: 
            return i
        last = c
    return -1


def isTidy (num: str):
    return findFirstDecreasingPointOf(num) == -1


def findAnswer (num: str):
    decreasingPoint = findFirstDecreasingPointOf(num)
    return num[:decreasingPoint] + str(int(num[decreasingPoint]) - 1) + ''.join(['9' for __ in num[decreasingPoint+1:]])


def trimZero(num: str):
    for i, x in enumerate(num):
        if x != '0':
            return num[i:]

if __name__ == '__main__':
    for tc in range(int(input())):
        x = input()
        while not isTidy(x):
            x = findAnswer(x)
        
        x = trimZero(x)
        print("Case #{0}: {1}".format(tc+1, x))