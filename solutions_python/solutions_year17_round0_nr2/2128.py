def Solve(num):
    digits = [int(x) for x in list(str(num))]
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            for j in range(i + 1, len(digits)):
                digits[j] = 9
            tmp = digits[i]
            for j in range(i, -1, -1):
                if j - 1 < 0 or digits[j - 1] < tmp:
                    digits[j] -= 1
                    break
                digits[j] = 9
    return "".join([str(x) for x in digits]).lstrip("0")

numOfLines = int(raw_input())
for i in range(numOfLines):
    num = int(raw_input())
    print "Case #" + str(i + 1) + ": " + str(Solve(num))

