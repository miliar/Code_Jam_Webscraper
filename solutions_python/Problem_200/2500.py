
for T in range(int(input())):
    val = input()

    testAgain = True
    while testAgain:
        L = len(val)
        R = int(val)
        tmp = 0
        testAgain = False
        for i in range(L-1):
            if int(val[i]) > int(val[i+1]):
                tmp = int(val[i+1:]) + 1
                val = str(R-tmp)
                testAgain = True
                break

    print("Case #%d: %d" %(T+1, R))
