__author__ = 'charles'

inputFile = "C-small-attempt0.in"
outputFile = inputFile + ".out"


class Recylce(object):

    def __init__(self, l, h):
        self.l = l
        self.h = h

    def DisplayCase(self):
        print "Case : min(" + str(self.l) + ") max(" + str(self.h) + ")"

    def SolveCase(self):
        hits = set()
        for i in range(self.l, self.h):
            for c in range (1, len(str(i))):
                pre = str(i)[len(str(i)) - c: len(str(i))]
                post = str(i)[0:len(str(i)) - c]
                checkint = int(pre + post)

                if checkint > i and checkint >= self.l and checkint <= self.h:
                   hits.add((i, checkint))

        return str(len(hits))

def extractTestCases(filename):

    with open(filename, 'r') as f:
        fileContents = (f.read().splitlines())
        f.close()

    cases = []
    for c in range(0,int(fileContents[0])):
        l, h = fileContents[c+1].split(" ")
        cases.append(Recylce(int(l), int(h)))

    return cases


def main():

    cases = extractTestCases(inputFile)


    for case in cases:
        print case.DisplayCase()


    with open(outputFile, "w") as w:
        for n in range(0, len(cases)):
            case = cases[n]
            print("Case #" + str(n + 1) + ": " + case.SolveCase() + "\n"),
            w.write("Case #" + str(n + 1) + ": " + case.SolveCase() + "\n")

if __name__ == "__main__":
    main()