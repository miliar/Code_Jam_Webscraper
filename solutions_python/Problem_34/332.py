import re

class AlienLanguage:
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile

        self.inf = open(infile, "r")
        self.readInput()
        self.inf.close()

        self.outf = open(outfile, "w")
        self.runTests()
        self.outf.close()


    def readInput(self):
        #first line
        firstline = self.inf.readline()
        flw = firstline.split()
        self.L = int(flw[0])
        self.D = int(flw[1])
        self.N = int(flw[2])

        # read D words
        self.words = []
        for i in range(self.D):
            self.words.append(self.inf.readline())

        #print self.words

        #read N test cases
        self.tests = []
        for i in range(self.N):
            self.tests.append(self.inf.readline())

        #print self.tests


    def runTests(self):
        tc = 1
        for test in self.tests:
            wmc = 0
            regexStr = '^' + test.rstrip().replace('(', '[').replace(')', ']') + '$'
            #print regexStr
            regex = re.compile(regexStr)
            for word in self.words:
                if regex.search(word):
                    wmc = wmc + 1
            #print "Case #" + str(tc) + ": " + str(wmc)
            self.outf.write("Case #" + str(tc) + ": " + str(wmc) + "\n")
            tc = tc + 1


if __name__ == "__main__":
    #al = AlienLanguage("in.txt", "out.txt")
    #asmall = AlienLanguage("A-small-attempt0.in", "A-small-attempt0.out")
    #alarge = AlienLanguage("Download A-large.in", "Download A-large.out")
    alarge = AlienLanguage("A-large.in", "A-large.out")
                
        
