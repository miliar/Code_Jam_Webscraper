inf = open("B-large.in", "r");
outf = open("googlers_out.txt", "w")
outf.close()

numSucc = 0

noCases = int(inf.readline())


#main
for j in range(0,noCases):
    #initialise
    numSucc = 0
    
    indata = inf.readline()
    info = indata.split()

    numGoo = int(info[0])
    numSur = int(info[1])
    minBest = int(info[2])
    tots = info[3:]

    i=0
    for number in tots:
        tots[i] = int(tots[i])
        i+=1

    # print numGoo, numSur, minBest, tots # REMOVE LATER

    for TotalScore in tots:
        if TotalScore == 0:
            if minBest == 0:
                numSucc+=1
        elif TotalScore >= ((3*minBest) - 2):
            numSucc+=1
        elif TotalScore >= ((3*minBest) - 4):
            if numSur != 0:
                numSucc+=1
                numSur-=1
        
    #print "Case #" + str(j+1) + ": " + str(numSucc)
    outf = open("googlers_out.txt", "a")
    outf.write("Case #" + str(j+1) + ": " + str(numSucc) + "\n")
    outf.close()

inf.close()
