# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for j in range(1, t + 1):
    [n] = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    listN = list(str(n))
    checkAgain = True
    makeNines = False
    startNineIndex = 0
    while checkAgain:
        checkAgain = False
        for i in range(len(listN) - 1):
            if listN[i] > listN[i+1]:
                #print("changing {} with {}".format(i, i+1))
                if i == 0 and listN[i] == 1:
                    listN[i] = ''
                else:
                    listN[i] = chr(ord(listN[i]) - 1)
                makeNines = True
                checkAgain = True
                startNineIndex = i+1
                break
        if makeNines:
            for i in range(startNineIndex, len(listN)):
                listN[i] = '9'
    print("Case #{}: {}".format(j, int("".join(listN))))
    # check out .format's specification for more formatting options
