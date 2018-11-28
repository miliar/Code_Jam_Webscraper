def ovation(inputfile, outputfile):
    print "bezig"
    inputdata = open(inputfile, "r")
    outputdata = open(outputfile, "w")
    T = int(inputdata.readline())
    for case in range(T):
        #read input
        U,N = inputdata.readline().split()
        mensen_recht = 0
        vrienden = 0
        for i in xrange(len(N)):
            if mensen_recht < i:
                vrienden += i - mensen_recht
                mensen_recht = i
            mensen_recht += int(N[i])

        outputdata.write("Case #" + str(case+1) + ": " + str(vrienden) + "\n")
    inputdata.close()
    outputdata.close()
    print "done"

ovation("As0.in","outputs.txt")
