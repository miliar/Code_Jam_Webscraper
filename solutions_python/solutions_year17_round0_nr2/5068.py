def isTidy(x):
    return list(str(x)) == sorted(str(x))

def lastTidy(n):
    print(n)
    i = n
    while (True):
        if isTidy(i):
            return i
        i -= 1
        print(i)

if __name__ == '__main__':
    with open("input.txt", 'r') as inputFile:
        inputLines = inputFile.readlines()

    with open("output.txt", 'w') as outputFile:
        for i in range(1, int(inputLines[0]) + 1):
            if len(inputLines[i].strip()):
                outputFile.write("Case #" + str(i) + ": " + str(lastTidy(int(inputLines[i]))) + '\n')
