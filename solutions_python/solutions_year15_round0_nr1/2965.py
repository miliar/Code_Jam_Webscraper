# *- encoding: utf-8 -*

class Solution():
    def solve(self, maxShyness, shynessBits):
        # shyness[idx] is the count audience of shyness idx
        shyness = [int(bit) for bit in shynessBits]

        invited = 0
        stoodCnt = 0
        # count from audience of shyness 0
        for shynessLevel in xrange(maxShyness + 1):
            # these audience need friends
            if stoodCnt < shynessLevel:
                newlyInvited = shynessLevel - stoodCnt
                invited += newlyInvited
                stoodCnt += newlyInvited
            stoodCnt += shyness[shynessLevel]
            # print invited, 'friends invited'
            # print stoodCnt, 'stood up'
        return invited

if __name__ == '__main__':
    outputFile = 'A-large.out'
    outputHandle = open(outputFile, 'w')
    # inputFile = 'A-small-practice.in'
    inputFile = 'A-large.in'
    inputHandle = open(inputFile, 'r')
    caseCnt = int(inputHandle.readline().strip())
    for caseIdx in xrange(caseCnt):
        tmp = inputHandle.readline().strip().split()
        outputHandle.write('Case #%d: %s\n' % (caseIdx + 1, Solution().solve(int(tmp[0]), tmp[1])))
    inputHandle.close()
    outputHandle.close()
