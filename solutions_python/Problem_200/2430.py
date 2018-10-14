def findTidy(num):
    decremented = False
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            decremented = True
        elif num[i] == num[i + 1]:
            for j in range(i + 1, len(num) - 1):
                if num[j] > num[j + 1]:
                    decremented = True
                    break
        if decremented:
            break
    if decremented:
        num[i] -= 1
        for j in range(i + 1, len(num)):
            num[j] = 9

with open("input.in") as finput, open("output.out", "w") as foutput:
    numCases = int(finput.readline().strip())
    for i in range(1, numCases + 1):
        num = list(map(int, list(finput.readline().strip())))
        findTidy(num)
        foutput.write("Case #" + str(i) + ": " + str(int("".join(map(str, num)))) + "\n")
