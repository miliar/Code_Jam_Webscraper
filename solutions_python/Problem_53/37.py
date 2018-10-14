def outputline(casenumber, ison, outlist):
    result = "Case #" + str(casenumber) + ": "
    if(ison):
        result += "ON"
    else:
        result += "OFF"
    outlist.append(result + '\n')

class Problem:
    def __init__(self):
        self.snappers = None
        self.snaps = None

def inputline(string, problemlist):
    args = string.split(' ')
    p = Problem()
    p.snappers = int(args[0])
    p.snaps = int(args[1])
    problemlist.append(p)

def compute(problem):
    return (problem.snaps+1) & ~(-1<<problem.snappers) == 0

def solution(inputfile,outputfile):
    inp = open(inputfile)
    p = Program()
    for line in inp:
        p.takeline(line)
    inp.close()
    p.compute()
    out = open(outputfile,'w')
    for line in p.outlines():
        out.write(line)
    out.close()

class Program:
    def __init__(self):
        self.count = None
        self.limit = None
        self.probs = []
        self.anss = []
        
        d = dict()
        def readT(string, program):
            program.curfunc = d["readP"]
            program.limit = int(string)
            program.count = 1
        def readP(string, program):
            inputline(string,program.probs)
            if(program.count > program.limit):
                raise Exception
            if(program.count == program.limit):
                program.curfunc = d["readT"]
            program.count += 1

        d["readT"] = readT
        d["readP"] = readP
        self.curfunc = d["readT"]

    def takeline(self,string):
        self.curfunc(string, self)

    def compute(self):
        casenum = 0
        for prob in self.probs:
            casenum += 1
            outputline(casenum,compute(prob),self.anss)

    def outlines(self):
        return self.anss
