from itertools import islice
import fractions as f

class Warning:

    n = 0 #number of cases
    N = 0 #number of events
    e = [] #time-elapsed-since-event array
    currcase = 0
    
    inputfile = "warning.in"
    outputfile = "warning.out"
    
    def __init__(self):
        self.solvetheproblem()

    def solvetheproblem(self):
        f = open(self.inputfile)
        g = open(self.outputfile,'a')

        with open(self.inputfile) as myfile:
            cases=list(islice(myfile,1))
            self.n = int(cases[0])

        for i in range(1,self.n+1):
            self.currcase = i
            with open(self.inputfile) as myfile:
                cases=list(islice(myfile,i,i+1))
                stuff = cases[0].split(" ")
                self.N = long(stuff[0])
                for p in range(1,self.N+1):
                    self.e.append(int(stuff[p]))

                diff = []
                self.e.sort()
                for q in range(0,len(self.e)-1):
                    diff.append(self.e[q+1]-self.e[q])
                T = self.mgcd(diff)
                print "Doing case.... " + str(self.currcase) + "\n"         
                seconds = (T-(self.e[0]%T))%T
                g.write("Case #" + str(i) + ": " + str(seconds) + "\n")
                self.e = []
                seconds = 0


    def mgcd(self,args):
        return reduce(f.gcd,args)
