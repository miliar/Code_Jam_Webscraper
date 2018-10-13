from itertools import islice

class ThemePark:

    n = 0 #number of cases
    R = 0 #number of rounds
    N = 0 #number of groups
    k = 0 #number of seats
    G = [] #the groups
    SG = [] #cumulative sums
    b = 0 #index at which you break the queue
    amount = 0 #what the roller coaster earns

    
    inputfile = "themepark.in"
    outputfile = "themepark.out"
    
    def __init__(self):
        self.solvetheproblem()

    def solvetheproblem(self):
        f = open(self.inputfile)
        g = open(self.outputfile,'a')

        with open(self.inputfile) as myfile:
            cases=list(islice(myfile,1))
            self.n = int(cases[0])

        j = 0
        for i in range(1,2*self.n,2):
            j = j + 1
            with open(self.inputfile) as myfile:
                cases=list(islice(myfile,i,i+2))
                print cases[0] + cases[1]
                stuff = cases[0].split(" ")
                groups = cases[1].split(" ")
                self.R = int(stuff[0])
                self.k = int(stuff[1])
                self.N = int(stuff[2])

                if(self.R == 0 or self.N == 0 or self.k == 0):
                    self.amount = 0
                    g.write("Case #" + str(j) + ": " + str(self.amount) + "\n")
                    continue
                
                
                self.G = []
                self.SG = []
                self.b = 0

                for y in range(0,self.N):
                    currgroup = int(groups[y])
                    self.G.append(currgroup)
                    
                
                self.computesum()
                #At this point, we have loaded all the data of case j onto
                #the class attributes. Now just solve this case:

                self.solve()
                g.write("Case #" + str(j) + ": " + str(self.amount) + "\n")
                self.amount = 0



    def solve(self):
        print "breakpoint = " + str(self.b) + ", " + str(self.N)
        for x in range(1,self.R):
            H = []
            self.SG = []
            leftover = self.N - self.b
            for q in range(0,self.N):                
                if(q < leftover):
                    H.append(self.G[q + self.b])
                else:
                    H.append(self.G[q - leftover])
                print H[q]
            
            self.G = H
            self.b = 0
            self.computesum()

            
    def computesum(self):
        for i in range(0,self.N):
            currgroup = self.G[i]
            if(self.b == 0):
               if(i > 0):
                    if (self.SG[i-1]+currgroup > self.k):
                        self.b = i
                    else:
                        self.SG.append(self.SG[i-1]+currgroup)
               else:
                   self.SG.append(currgroup)
        if(self.b == 0):
            self.amount = self.amount + self.SG[self.N-1]
        else:
            self.amount = self.amount + self.SG[self.b-1]
        print "new bp: " + str(self.b)

