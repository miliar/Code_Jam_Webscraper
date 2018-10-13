import sys, math

def stalls(n, k):
    largestPowerOf2 = 2 ** int(math.log(k, 2))
    numBefore = largestPowerOf2 - 1
    numNow = k - numBefore

    smallerGap = int((n - numBefore) / largestPowerOf2)
    numLargerGap = (n - numBefore) % largestPowerOf2
    isLarger = True if numNow <= numLargerGap else False

    gap = smallerGap + 1 if isLarger else smallerGap
    return str(int(math.ceil((gap - 1) / 2.0))) + ' ' + str(int(math.floor((gap - 1) / 2.0)))

if __name__ == '__main__':
    test = open(sys.argv[1], 'r')
    for i in range(int(test.readline().strip())):
        n, k = test.readline().split(' ')
        print('Case #' + str(i + 1) + ': ' + str(stalls(int(n), int(k))))
