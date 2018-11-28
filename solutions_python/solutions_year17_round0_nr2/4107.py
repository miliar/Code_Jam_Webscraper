def doSomething(a):

    newNumber = ""

    for i in range(0, len(a)):
        if i < len(a) - 1:
            if int(a[i]) > int(a[i + 1]):
                newNumber += str(int(a[i]) - 1)
                for j in range(i + 1, len(a)):
                    newNumber += "9"
                break
            else:
                newNumber += a[i]
        else:
            newNumber += a[i]

    a = newNumber
    newNumber = ""

    roubaUm = False
    for i in range(len(a) - 1, -1, -1):

        newNum = int(a[i])

        if i > 0:
            if (int(a[i]) < int(a[i - 1])) or (roubaUm and int(a[i]) - 1 < int(a[i - 1])):
                newNum = 9
                roubaUm = True
            elif roubaUm:
                newNum -= 1
                roubaUm = False
        elif roubaUm:
            newNum -= 1

        newNumber = str(newNum) + newNumber

    return str(int(newNumber))


t = int(input())

for i in range(1, t + 1):
    a = input()

    print("Case #{}: {}".format(i, doSomething(a)))
