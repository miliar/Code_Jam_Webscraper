import sys

def main():
    if(len(sys.argv) < 2):
        print("Not enough arguments. Exiting.")
        exit()
    file = open(sys.argv[1], 'r')

    totalCases = int(file.readline().strip())
    testCases = 0

    line = file.readline().strip()
    while(line != ""):
        testCases += 1
        line = [int(i) for i in list(line)]

        lineLen = len(line)
        for i in range(1, lineLen):
            if(line[lineLen - i - 1] > line[lineLen - i]):
                line[lineLen - i - 1] -= 1
                for j in range(i):
                    line[lineLen - i + j] = 9

        line = [str(i) for i in list(line)]
        print("Case #" + str(testCases) + ": " + str(int("".join(line))))
        line = file.readline().strip()

    file.close()

if(__name__ == "__main__"):
    main()
