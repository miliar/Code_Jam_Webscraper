import string

def cookieCounter(txtFile):
    infile = open(txtFile, "r")
    testCases = int(infile.readline())
    
    for i in range(testCases):
        variables = infile.readline()
        variables = string.split(variables, " ")
        farmCost = float(variables[0])
        farmRate = float(variables[1])
        win = float(variables[2])
        cps = 2.0
        numFarm = 0
        upkeep = 0
        prior = win
        new = win/2.0
        
        while prior > new:
            upkeep += farmCost/cps
            numFarm += 1
            cps += farmRate
            prior = new
            new = (win/cps)+upkeep
            
            
        print "Case #" + str(i+1) + ": %0.7f" % (prior)
        

cookieCounter("cookieTest.txt")    