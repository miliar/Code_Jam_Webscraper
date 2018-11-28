__author__ = 'Anand Mani Sankar'


def solve(test):
    data = test.split()
    highestShyIndex = int(data[0])
    inputData = data[1]
    sumTillNow = int(inputData[0])
    minReq = 0

    #print "index = %d, current value = %d, min req = %d and sum till now = %d" % (0, int(inputData[0]), minReq, sumTillNow)

    for i in range(1, highestShyIndex + 1):

        #print "index = %d, current value = %d, min req = %d and sum till now = %d" % (i, int(inputData[i]), minReq, sumTillNow)

        if i > (sumTillNow + minReq):
            minReq += 1

        sumTillNow += int(inputData[i])

    return str(minReq)



def main():
    inputfile = open('A-large.in', 'r')
    outputfile = open('output.txt','w')
    tests = int(inputfile.readline())
    for count in range(0, tests):
        case = count + 1
        result = solve(inputfile.readline())
        outputfile.write('Case #' + str(case) + ": " + result + '\n')


if __name__ == '__main__':
    main()
