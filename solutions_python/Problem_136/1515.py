import sys

if __name__ == "__main__":
    inputFile = sys.argv[1]
    outputFile = inputFile.split('.')[0] + '.out'
    outputFileStream = open(outputFile,'w')

    with open(inputFile,'r') as inputFileStream:
        N = int(inputFileStream.next())
        for k in range(N):
            C, F, X = [float(x) for x in inputFileStream.next().split()]
            rate, time = 2.0, 0.0
            while True:
                t1 = X/rate
                t2 = C/rate 
                if t1 < t2 + X/(rate + F):
                    time = time + t1
                    break
                else:
                    time = time + t2
                    rate = rate + F

            ans = '%.7f' % time
            outputString = 'Case #' + str(k+1) + ': ' + ans
            # print outputString
            outputFileStream.write(outputString + '\n')
