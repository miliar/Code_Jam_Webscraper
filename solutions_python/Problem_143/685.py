__author__ = 'Drazen'


def solve(A, B, K):
    result = 0;
    for i in range(A):
        for j in range(B):
            if ((i & j) < K):
                result += 1
    return str(result)



if __name__ == "__main__":
    inputFile = open('H:/development/GoogleCodeJam/2014/round1B/B/B-small-attempt0.in', mode='r')
    outputFile = open('H:/development/GoogleCodeJam/2014/round1B/B/output.txt', mode='w')
    resultLine = 'Case #{0}: {1}'
    inputFile.seek(0)
    numberOfTests = int(inputFile.readline())
    for i in range(numberOfTests):
        A, B, K = map(int, inputFile.readline().split())
        outputFile.write( str.format(resultLine, i+1, solve(A,B,K) + '\n'))
    inputFile.close()
    outputFile.close()