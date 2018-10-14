def checkForTidy(number):
    digits = []
    while number >= 1:
        d = number % 10
        number /= 10
        digits.append(d)
    if len(digits) == 1:
        return True
    for i in range(0, len(digits) - 1):
        if digits[i] < digits[i+1]:
            return False
    return True

def makeTidy(number):
    digits = []
    while number >= 1:
        d = number % 10
        number /= 10
        digits.append(d)
    digits.reverse()
    while True:
        check = True
        pos = 0
        for i in range(0, len(digits) - 1):
            if digits[i] > digits[i+1]:
                check = False
                pos = i
                break
        if check:
            return makeNumberFromDigits(digits)
        tmpNumber = digits[pos]*10 + digits[pos+1]
        while not checkForTidy(tmpNumber):
            tmpNumber -= 1
        digits[pos+1] = tmpNumber%10
        digits[pos] = tmpNumber/10
        for i in range(pos+2, len(digits)):
            digits[i] = 9

def makeNumberFromDigits(digits):
    result = 0
    for i in range(0, len(digits)):
        result *= 10
        result += digits[i]
    return result

T = raw_input()
for t in range(0, (int(T))):
    inputString = raw_input()
    N = int(inputString)
    print "Case #" + str(t+1) + ": " + str(makeTidy(N))
