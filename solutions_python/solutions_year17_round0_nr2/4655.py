def main():
    textFile = open('SmallOutput.in', 'w')
    for caseNum in range(int(input())):
        number = input()
        if len(number) == 1 or sorted(number) == list(number):
            textFile.write("Case #" + str(caseNum + 1) + ": " + number + "\n")
            continue

        keyOfFirstError = findFirstErr(number)
        success = solveError(number, keyOfFirstError)
        textFile.write("Case #" + str(caseNum + 1) + ": " + (str(success)) + "\n")
    textFile.close()


def solveError(number, keyOfFirstError, res='', updated=False):
    if keyOfFirstError > len(number) - 1:
        return res

    if keyOfFirstError > 0 and updated == False:
        res = number[:keyOfFirstError]


    if int(number[keyOfFirstError]) > 1:
        if updated == False:
            res += str((int(number[keyOfFirstError])) - 1)
        else:
            res += "9"
        return solveError(number, keyOfFirstError + 1, res, True)
    else:
        if keyOfFirstError == 0:
            num = [9 for i in range(len(number))]
        else:
            num = list(number)
            num[keyOfFirstError-1] = str(int(num[keyOfFirstError-1]) -1)
            num[keyOfFirstError] = str(9)
            keyOfFirstError -= 1

        return solveError(num, keyOfFirstError + 1, res, True)

    return res


def findFirstErr(number):
    for key, value in enumerate(number):
        if key < len(number) - 1 and int(value) > int(number[key + 1]):
            if "9" in number and number.index("9") < key:
                return number.index("9")
            elif number.index(value) == key - 1:
                return number.index(value)
            else:
                return key

    return None


if __name__ == '__main__':
    main()

