
def checkTidy(num):
    """Returns true is num is tidy, false otherwise"""

    num = [int(n) for n in list(str(num))]

    for i in range(len(num) - 1, 0, -1):
        if num[i]<num[i-1]:
            return False

    return True

numCases = raw_input()
for n in range(int(numCases)):
    number = raw_input()
    number = int(number)

    while number != 0:
        tidy = checkTidy(number)
        if tidy:
            break
        number = number - 1

    print "Case #{}: {}".format(n+1, number)
