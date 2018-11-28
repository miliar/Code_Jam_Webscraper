def readFile(flname):
    lines = open(flname).read().split("\n")
    outputfl = open("output.txt","w")
    testAmount = int(lines[0])
    i=1
    tstNum = 1
    while tstNum <=testAmount:
        curTest = lines[i].split(" ")
        (d,n) = (int(curTest[0]),int(curTest[1]))
        players = [(int(ln.split(" ")[0]),int(ln.split(" ")[1])) for ln in lines[i+1:i+n+1]]
        curAns = solveSpecificRow(d,players)
        outputfl.write("Case #"+str(tstNum)+": "+str(curAns)+"\n")
        i+=+n+1
        tstNum+=1
    outputfl.close()
def solveSpecificRow(d,players):
    timesToFin = [float(d-ki)/si for (ki,si) in players]
    maxTime = max(timesToFin)
    return d/maxTime
