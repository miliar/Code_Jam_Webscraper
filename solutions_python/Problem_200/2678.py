import sys

sys.stdin = open("B-large.in", "r")
sys.stdout = open("sol", "w")

def isTidy(digits):
    for i in range(1, len(digits)):
        if digits[i] < digits[i-1]:
            return False

    return True

def toDigits(num):
    return list(map(int, str(num)))

def toNum(digits):
    return int(''.join(map(str, digits)))

def solve(num):
    if isTidy(toDigits(num)):
        return num

    maxNum = num

    digits = toDigits(num)
    for j in range(len(digits) - 1, -1, -1):
        while (num > maxNum or not isTidy(digits)) and digits[j] != 9:
            num -= 1 * pow(10, len(digits) - j - 1)
            digits = toDigits(num)

    return toNum(digits)

T = int(input())

for t in range(T):
    num = int(input())
    print("Case #" + str(t+1) + ":", solve(num))