class Stalls:
    def __init__(self, N, K):
        self.stallsArray = ['X'] + [None] * N + ['X']
        for i in range(1, K+1):
            left, right, max = self.determineSpot(i)
            currentSpot = left+(max-1)//2
            self.stallsArray[currentSpot] = 'X'
            if i == K:
                self.max, self.min = self.getOpenStalls(currentSpot)

    def determineSpot(self, num):
        max = 0
        mover = 1
        rightEnd = len(self.stallsArray) - 1
        returnLeft, returnRight = mover, rightEnd

        while mover < rightEnd:
            currentLeft = mover
            countEmpty = 0
            while self.stallsArray[mover] is None:
                mover = mover + 1
                countEmpty = countEmpty + 1
            currentRight = mover - 1
            mover = mover + 1
            if countEmpty > max:
                returnLeft = currentLeft
                returnRight = currentRight
                max = countEmpty
                if rightEnd < max + countEmpty:
                    break
        return returnLeft, returnRight, max

    def getOpenStalls(self, spot):
        moveLeft = spot - 1
        moveRight = spot + 1
        countLeft = countRight = 0
        while self.stallsArray[moveLeft] is None:
            moveLeft = moveLeft - 1
            countLeft = countLeft + 1
        while self.stallsArray[moveRight] is None:
            moveRight = moveRight + 1
            countRight = countRight + 1
        return max(countLeft, countRight), min(countLeft, countRight)


if __name__ == '__main__':
    with open('stallsinput.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for i in range(1, int(content[0])+1):
        (N,K) = content[i].split()
        scenario = Stalls(int(N), int(K))
        print 'Case #{0}: {1} {2}'.format(i, scenario.max, scenario.min)
