from itertools import islice

class Snapper:

    n = 0 #number of cases
    N = 0 #number of snappers
    K = 0 #number of snaps
    currcase = 0
    
    inputfile = "snapper.in"
    outputfile = "snapper.out"
    
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
                self.N = int(stuff[0])
                self.K = int(stuff[1])
                initial = pow(2,self.N)-1
                if(self.K < initial):
                    g.write("Case #" + str(i) + ": OFF\n")
                elif(self.K == initial):
                    g.write("Case #" + str(i) + ": ON\n")
                else:
                    if((self.K - initial)%(pow(2,self.N)) == 0):
                        g.write("Case #" + str(i) + ": ON\n")
                    else:
                        g.write("Case #" + str(i) + ": OFF\n")
                    
