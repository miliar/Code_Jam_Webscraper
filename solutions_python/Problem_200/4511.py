import sys

n = int(input())

def findtidy(num, digit, index):
    a = int(str(num)[index])
    b = int(str(num)[index-1])

    while(a < b and a >= 0):
        a -= 1
        num -= 10**digit
        if digit > 0:
            num += (10**digit - 1) - num % (10 ** digit)

    return num

def findall(num):
    l = len(str(num))
    for digit in range(l - 1):
        index = l - digit - 1
        num = findtidy(num, digit, index)

    return num

def checkdigit(num):
    s = str(num)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False

    return True

for i in range(1, n+1):
    num = int(input())
    l = len(str(num))

    while not checkdigit(num):
        num = findall(num)

    print("Case #%d: %d" % (i, num))


