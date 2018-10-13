import sys

"""
def getNumb(N):
    N = str(N)
    currNum = "1"
    currSteps = 1
    if len(currNum) == len(N):
        if currNum[:len(currNume) / 2] == N[:len(N) / 2]:
            currStep += int(N[len(N) / 2:]) - int(N[len(currNum) / 2:])
            return currStep
        else:
            currStep += reverse(N[:len(N) / 2])

"""
class Answer(object):


    def getNumb(self, N):
        curr, result = 1, 1
        toCheck = []
        visited = {}
        fresult = sys.maxint
        toCheck.append((curr, result))
        currInd = 0
        while toCheck[currInd:]:
            curr, result = toCheck[currInd]
            currInd += 1
            if curr <= N:
                if curr == N:
                    if result < fresult:
                        fresult = result
                else:
                    if curr + 1 not in visited:
                        visited[curr + 1] = result + 1
                        toCheck.append((curr + 1, result + 1))
                    revCurr = int(str(curr)[::-1])
                    if revCurr <= N and revCurr not in visited:
                        visited[revCurr] = result + 1
                        toCheck.append((revCurr, result + 1))
        return fresult

    def getAnswer(self):
        fOutput = open('Output.txt', 'w')
        fInput = open('A-small-attempt6.in')
        testCount = int(fInput.readline())
        test = 0
        for line in fInput:
            N = int(line)
            result = self.getNumb(N)
            fOutput.write("Case #{test}: {result}\n".format(test=test + 1, result=result))
            test += 1
        fInput.close()
        fOutput.close()

a = Answer()
print a.getAnswer()