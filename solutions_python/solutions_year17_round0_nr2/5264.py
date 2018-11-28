count = int(input())

def convert(numList):
    num = int(''.join(map(str, numList)))
    return num

for x in range(count):
    check = False
    y = [int(x) for x in input()]
    for i in range(len(y) - 1):
        if not check:
            if y[i + 1] < y[i]:
                prev = i - 1
                test = y[i]
                if(prev >= 0):
                    while(test == y[prev]):
                        if(prev == 0):
                            y[i] = 10
                            y[prev] = y[prev] - 1
                            break
                        y[prev] = 9
                        prev = prev - 1
                        y[i] = 10

                y[i] = y[i] - 1
                y[len(y) - 1] = 9
                check = True
        else:
            y[i] = 9

    print("Case #" + str(x + 1) + ": " + str(convert(y)))

