import os


class JamFileProcessor:
    casenum = 0

    def __init__(self, problem, input_type, lines_per_case):
        self.infile = open("/home/oskar/Downloads/{0}-{1}.in".format(problem, input_type), "r")
        outfilename = "../../../out/result.out"
        if os.path.exists(outfilename):
            os.remove(outfilename)
        self.outfile = open(outfilename, "a")
        self.cases = int(self.infile.readline())
        self.lines_per_case = lines_per_case

    def readcase(self):
        args = []
        self.casenum += 1
        for i in range(self.lines_per_case):
            line = self.infile.readline()

            if line:
                line = line.rstrip()
                args.append(line.split(" "))
            else:
                return False
        args.append(self.casenum)
        return args

    def appendline(self, text):
        self.outfile.write(text + "\n")

    def writecase(self, result):
        self.appendline("Case #{0}: {1}".format(self.casenum, result))
