numOfProblem = input()


def isNotTidy(number):
    if (number < 10):
        return False

    lastDigit = 9
    while number:
        digit = number % 10
        if (digit <= lastDigit):
            lastDigit = digit
            number //= 10
        else:
            return True

    return False


for i in range(0, numOfProblem, 1):
    lastCount = input()

    while (isNotTidy(lastCount)):
        lastCount = lastCount - 1

    output = 'Case #' + str(i + 1) + ': ' + str(lastCount)
    print output
