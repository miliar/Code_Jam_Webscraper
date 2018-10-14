def getNum(size):
    currentNum = int(size)
    while currentNum > 0:
        if isNonDecreasing(currentNum):
            return currentNum
        currentNum -= 1
    return 0

def isNonDecreasing(num):
    numList = [int(digit) for digit in str(num)]
    lastLetter = numList[0]
    for i in numList[1:]:
        if i < lastLetter:
            return False
        lastLetter = i
    return True

if __name__ == "__main__":
    t = int(input())  # read a line with a single integer
    f = open('out.txt', 'w')
    for i in range(1, t + 1):
        n = input()
        print("Case #{}: {} ".format(i, getNum(n)))
        f.write("Case #{}: {} \n".format(i, getNum(n)))
    f.close()
