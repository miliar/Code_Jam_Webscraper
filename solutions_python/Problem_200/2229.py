def checkDigits(digits):
    for c in range(0,len(digits) - 1):
        if digits[c] > digits[c + 1]:
            return False
    return True

def fixDigits(digits):
    done = False
    current = 0
    while not done and current < len(digits) - 1:
        if digits[current] > digits[current + 1]:
            done = True
            digits[current] -= 1
            for place in range(current + 1, len(digits)):
                digits[place] = 9
        current += 1;
    return digits

with open('in') as f:
    caseCounter = 0
    for line in f:
        if caseCounter != 0:
            digits = list(map(int, line[:len(line)-1]))
            while not checkDigits(digits):
                digits = fixDigits(digits)
            print("Case #" + str(caseCounter) + ": " + str(int("".join(map(str, digits)))))
        caseCounter += 1
