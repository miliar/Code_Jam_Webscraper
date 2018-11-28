def removeStr(list, str):
    for s in str:
        list.remove(s)

def removeNum(list, num):
    if num == 0:
        removeStr(list, 'ZERO')
    if num == 1:
        removeStr(list, 'ONE')
    if num == 2:
        removeStr(list, 'TWO')
    if num == 3:
        removeStr(list, 'THREE')
    if num == 4:
        removeStr(list, 'FOUR')
    if num == 5:
        removeStr(list, 'FIVE')
    if num == 6:
        removeStr(list, 'SIX')
    if num == 7:
        removeStr(list, 'SEVEN')
    if num == 8:
        removeStr(list, 'EIGHT')
    if num == 9:
        removeStr(list, 'NINE')

def hasNum(list, num):
    if num == 0:
        return 'Z' in list
    if num == 6:
        return 'X' in list
    if num == 7:
        return 'S' in list
    if num == 2:
        return 'W' in list
    if num == 8:
        return 'G' in list
    if num == 3:
        return 'T' in list
    if num == 4:
        return 'U' in list
    if num == 5:
        return 'F' in list
    if num == 9:
        return 'I' in list
    if num == 1:
        return 'O' in list
    return False

def getDigits(list, num):
    if not list:
        return num
    else:
        if hasNum(list, 0):
            num.append(0)
            removeNum(list, 0)
            return getDigits(list, num)
        if hasNum(list, 6):
            num.append(6)
            removeNum(list, 6)
            return getDigits(list, num)
        if hasNum(list, 7):
            num.append(7)
            removeNum(list, 7)
            return getDigits(list, num)
        if hasNum(list, 2):
            num.append(2)
            removeNum(list, 2)
            return getDigits(list, num)
        if hasNum(list, 8):
            num.append(8)
            removeNum(list, 8)
            return getDigits(list, num)
        if hasNum(list, 3):
            num.append(3)
            removeNum(list, 3)
            return getDigits(list, num)
        if hasNum(list, 4):
            num.append(4)
            removeNum(list, 4)
            return getDigits(list, num)
        if hasNum(list, 5):
            num.append(5)
            removeNum(list, 5)
            return getDigits(list, num)
        if hasNum(list, 9):
            num.append(9)
            removeNum(list, 9)
            return getDigits(list, num)
        if hasNum(list, 1):
            num.append(1)
            removeNum(list, 1)
            return getDigits(list, num)


def getDigit(s):
    num = sorted(getDigits(list(s), []))
    return ''.join(str(x) for x in num)

def main():
    t = int(input())
    for i in range(1, t+1):
        case = input()
        print("Case #{}: {}".format(i, getDigit(case)))

if __name__ == "__main__":
    main()