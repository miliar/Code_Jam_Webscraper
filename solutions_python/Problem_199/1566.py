def flip(cakeStr, pos):
    if cakeStr[pos] == "+":
        cakeStr = cakeStr[:pos] + "-" + cakeStr[(pos+1):]
        #cakeStr[pos].replace("+", "-")
        #cakeStr[pos] = "-"
    else:
        cakeStr = cakeStr[:pos] + "+" + cakeStr[(pos+1):]
        #cakeStr[pos].replace("-", "+")
        #cakeStr[pos] = "+"
    return cakeStr


def calFlip(cakeStr, K):
    i = 0
    count = 0
    while i <= (len(cakeStr) - K):
        if cakeStr[i] == "-":
            count += 1
            for j in range(0, K):
                cakeStr = flip(cakeStr, i + j)
        i += 1
    while i < len(cakeStr):
        if cakeStr[i] == "-":
            return -1
        i += 1
    return count

T = raw_input()
for t in range(0, (int(T))):
    inputString = raw_input()
    inputString = inputString.split()
    cakeStr = inputString[0]
    K = int(inputString[1])
    result = calFlip(cakeStr, K)
    if result == -1:
        print "Case #" + str(t+1) + ": IMPOSSIBLE"
    else:
        print "Case #" + str(t+1) + ": " + str(result)






