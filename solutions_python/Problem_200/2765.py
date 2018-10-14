def isTidy(n):
    max = 9
    while (n!=0):
        i = n % 10
        n //= 10
        if (i > max):
            return False
        else:
            max = i
    return True

if __name__ == '__main__':
    tinySet = []
    for i in range(0, 1000):
        if (isTidy(i)):
            tinySet.append(i)

    testNum = int(input())
    for i in range(1, testNum + 1):
        N = int(input())
        while True:
            if (N in tinySet):
                print("Case #" + str(i) + ": " + str(N))
                break
            else:
                N -= 1

