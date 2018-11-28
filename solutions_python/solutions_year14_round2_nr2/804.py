import sys

if __name__ == '__main__':
    inputFile = open(sys.argv[1],'r')
    outputFile = open("output.txt", 'w')

    numCases = int(inputFile.readline())

    for i in range(numCases):
        print("Case #"+str(i+1)+": ")
        outputFile.write("Case #"+str(i+1)+": ")

        inputNum = [int(x) for x in inputFile.readline().strip('\n').split()]
        A = inputNum[0]
        B = inputNum[1]
        K = inputNum[2]

        result = 0

        for i in range(A):
            for j in range(B):
                if (i & j) < K:
                    result += 1

        print(str(result))
        outputFile.write(str(result)+'\n')
