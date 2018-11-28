import sys

def addMinutes(strTime, intMinutes):
    h, m = strTime.split(":")
    h = int(h)
    m = int(m) + intMinutes
    if m >= 60:
        h = h + 1
        m = m - 60
    return "%02d:%02d"%(h, m)

if __name__ == "__main__":
    strInputFile = "input.txt"
    strOutputFile = "output.txt"

    try:
        inputFile = open(strInputFile, "r")
        N = int(inputFile.readline())
    except:
        print "Error with file reading : Reading TC count failed"
        sys.exit()
    
    try:
        outputFile = open(strOutputFile, "w")
    except:
        print "Error with file writing : File creation failed"
        sys.exit()
        
    i = 1
    while i <= N:
        #read the test case
        try:
            T = int(inputFile.readline())
            NA, NB = inputFile.readline().split(" ")
        except:
            print "Error with file reading : Reading T, NA, NB failed"
            sys.exit()
            
        NA = int(NA)
        NB = int(NB)
        NAlist = []
        NBlist = []

        while NA:
            NAlist.append(inputFile.readline().rstrip())
            NA -= 1
        
        while NB:
            NBlist.append(inputFile.readline().rstrip())
            NB -= 1
        
        #print NAlist, NBlist
        NAstart = []
        NApool = []
        NBstart = []
        NBpool = []

        for jtime in NAlist:
            jtimelist = jtime.split(" ")
            NAstart.append(jtimelist[0])
            NBpool.append(addMinutes(jtimelist[1], T)) #add turn around time
              
        for jtime in NBlist:
            jtimelist = jtime.split(" ")
            NBstart.append(jtimelist[0])
            NApool.append(addMinutes(jtimelist[1], T)) #add turn around time
        
        NAstart.sort()
        NApool.sort()
        NBstart.sort()
        NBpool.sort()
        
        NAneed = NBneed = 0
        
        for train in NAstart:
            if NApool and train >= NApool[0]:
                del NApool[0]
            else:
                NAneed += 1
                
        for train in NBstart:
            if NBpool and train >= NBpool[0]:
                del NBpool[0]
            else:
                NBneed += 1
              
        try:
            outputFile.write("Case #%d: %d %d\n"%(i, NAneed, NBneed))
        except:
            print "Error with file writing : result not written"
            sys.exit()
            
        i += 1
        #end of tc loop
    outputFile.close()
    inputFile.close()