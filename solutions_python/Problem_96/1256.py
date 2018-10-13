__author__ = 'charles'

inputFile = "B-large.in"
outputFile = inputFile + ".out"

class Dance(object):

    def __init__(self, surprises, targetBestScore, danceCards):
        self.surprises = int(surprises)
        self.targetBestScore = int(targetBestScore)
        self.danceCards = danceCards

    def DisplayCase(self):

        print "Case : [surprises:" + str(self.surprises) + "] - [target:" + str(self.targetBestScore) + "]"
        print ",".join(self.danceCards)

    def SolveCase(self):
        matched = 0
        for card in self.danceCards:


            cardAv = int(card) / 3

            maxWithoutSurprise = 0
            maxWithSurprise = 0

            if int(card) == 0:
                maxWithoutSurprise = 0
                maxWithSurprise = 0

            elif int(card) == 1:
                maxWithoutSurprise = 1
                maxWithSurprise = 1

            elif int(card) == 2:
                maxWithoutSurprise = 1
                maxWithSurprise = 2

            elif int(card) % 3 == 0:
                maxWithoutSurprise = cardAv
                maxWithSurprise = cardAv + 1

            elif int(card) % 3 == 1:
                maxWithoutSurprise = cardAv + 1
                maxWithSurprise = cardAv + 1

            elif int(card) % 3 == 2:
                maxWithoutSurprise = cardAv + 1
                maxWithSurprise = cardAv + 2

            if maxWithoutSurprise >= self.targetBestScore:
                matched += 1

            elif maxWithSurprise >= self.targetBestScore and self.surprises > 0:
                matched += 1
                self.surprises -= 1

            print card, cardAv, maxWithoutSurprise, maxWithSurprise, matched, self.surprises
        return str(matched)


def extractTestCases(filename):

    with open(filename, 'r') as f:
        fileContents = (f.read().splitlines())
        f.close()

    cases = []
    for c in range(0,int(fileContents[0])):
        dd = fileContents[c+1].split(" ")
        cases.append(Dance(dd[1], dd[2], dd[3:]))

    return cases


def main():

    cases = extractTestCases(inputFile)


   # for case in cases:
    #    print case.DisplayCase()


    with open(outputFile, "w") as w:
        for n in range(0, len(cases)):
            case = cases[n]
            w.write("Case #" + str(n + 1) + ": " + case.SolveCase() + "\n")

if __name__ == "__main__":
    main()