__author__ = 'charles'

inputFile = "a-small-attempt0.in"
outputFile = inputFile + ".out"

translated = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvy qeez'
orriginal =  'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upa zooq'

trans = {}

for i,v in enumerate(translated):
    trans[v] = orriginal[i]

class Translate(object):

    def __init__(self, text):
        self.text = text

    def DisplayCase(self):
        print "Case : " + ",".join(self.text)

    def SolveCase(self):
        reverse = ""
        for c in self.text:
            reverse += trans[c]

        return reverse

def extractTestCases(filename):

    with open(filename, 'r') as f:
        fileContents = (f.read().splitlines())
        f.close()

    cases = []
    for c in range(0,int(fileContents[0])):
        cases.append(Translate(fileContents[c+1]))

    return cases

def main():
    cases = extractTestCases(inputFile)


    for case in cases:
        print case.DisplayCase()


    with open(outputFile, "w") as w:
        for n in range(0, len(cases)):
            case = cases[n]
            w.write("Case #" + str(n + 1) + ": " + case.SolveCase() + "\n")

if __name__ == "__main__":
    main()