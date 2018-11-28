def outputline(casenumber, euros, outlist):
    result = "Case #" + str(casenumber) + ": " + str(euros)
    outlist.append(result + '\n')

class Problem:
    def __init__(self):
        self.times = None
        self.maxload = None
        self.grouplist = list()

def inputline(string, problemlist):
    args = string.split()
    p = Problem()
    p.times = int(args[0])
    p.maxload = int(args[1])
    listsize = int(args[2])
    for groupsize in args[3:]:
        p.grouplist.append(int(groupsize))
    if(listsize != len(p.grouplist)):
        raise Exception
    problemlist.append(p)

class Ride:
    def __init__(self,startindex):
        self.nextindex = startindex
        self.peopleaboard = 0

class Cycle:
    def __init__(self):
        self.rides = 0
        self.people = 0

class Results:
    def __init__(self, ridesleft):
        self.ridesleft = ridesleft
        self.filled = 0
    def addpeople(self, people):
        self.filled += people

def compute(problem):
    cyclepoint, ridemap = computecyclepoint(problem.maxload,problem.grouplist)
    cycle = computecycledata(ridemap, cyclepoint)
    r = Results(problem.times)
    ridehead(ridemap, cyclepoint, r)
    ridecycle(cycle, r)
    ridetail(ridemap, cyclepoint, r)
    return r.filled

def ridehead(ridemap, cyclepoint, results):
    index = 0
    while(cyclepoint != index):
        results.ridesleft -= 1
        ride = ridemap[index]
        results.addpeople(ride.peopleaboard)
        index = ride.nextindex

def ridecycle(cycle, results):
    results.addpeople((results.ridesleft // cycle.rides) * cycle.people)
    results.ridesleft = results.ridesleft % cycle.rides

def ridetail(ridemap, cyclepoint, results):
    index = cyclepoint
    while(results.ridesleft > 0):
        results.ridesleft -= 1
        ride = ridemap[index]
        results.addpeople(ride.peopleaboard)
        index = ride.nextindex

def computecyclepoint(maxload, grouplist):
    index = 0
    listlength = len(grouplist)
    indexset = set()
    ridemap = dict()
    while(index not in indexset):
        indexset.add(index)
        currentride = Ride(index)
        ridemap[index] = currentride
        groupcount = 0
        peoplecount = 0
        keeploading = True
        while(groupcount < listlength and keeploading):
            if(peoplecount + grouplist[index] > maxload):
                keeploading = False
            else:
                peoplecount += grouplist[index]
                groupcount += 1
                index = (index + 1) % listlength
                currentride.peopleaboard = peoplecount
                currentride.nextindex = index
    return index, ridemap

def computecycledata(ridemap, cyclepoint):
    c = Cycle()
    keepgoing = True
    index = cyclepoint
    while(keepgoing):
        c.rides += 1
        c.people += ridemap[index].peopleaboard
        index = ridemap[index].nextindex
        if(index == cyclepoint):
            keepgoing = False
    return c

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
        self.buffer = None
        self.probs = []
        self.anss = []
        
        d = dict()
        def readT(string, program):
            program.curfunc = d["readP1"]
            program.limit = int(string)
            program.count = 1
        def readP1(string, program):
            program.buffer = string
            program.curfunc = d["readP2"]
        def readP2(string, program):
            inputline(program.buffer + string,program.probs)
            if(program.count > program.limit):
                raise Exception
            if(program.count == program.limit):
                program.curfunc = d["readT"]
            else:
                program.curfunc = d["readP1"]
            program.count += 1

        d["readT"] = readT
        d["readP1"] = readP1
        d["readP2"] = readP2
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
