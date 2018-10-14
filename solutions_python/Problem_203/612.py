# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def formatted(answer, case_num):
    print("Case #{}:".format(case_num))
    for i in answer:
        print("".join(i))

def answer(line):
    dimsList = line.split(" ")
    R = int(dimsList[0])
    C = int(dimsList[1])
    finalList = []
    for i in range(R):
        tempList = list(input())
        ##print('test {}'.format(tempList))
        lastChar = None
        keeperList = []
        for j in range(len(tempList)):
            ##print("test2 {}".format(keeperList))
            if tempList[j] != "?":
                lastChar = tempList[j]
                while len(keeperList) != 0:
                    temp_val = keeperList.pop()
                    tempList[temp_val] = lastChar
            else:
                if lastChar != None:
                    tempList[j] = lastChar
                else:
                    keeperList.append(j)
        finalList.append(tempList)

    ##print("{} {} {} {}".format(C, ))
    for i in range(C):
        lastChar = None
        keeperList = []
        for j in range(R):
            if finalList[j][i] != "?":
                lastChar = finalList[j][i]
                while len(keeperList) != 0:
                    temp_val = keeperList.pop()
                    finalList[temp_val[0]][temp_val[1]] = lastChar
            else:
                if lastChar!= None:
                    finalList[j][i] = lastChar
                else:
                    keeperList.append((j, i))

    return finalList

    ## Return a list of strings.

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    line = input()
    formatted(answer(line), i)
