inf = open("C-small-attempt3.in", "r")
outf = open("recnumbers_out.txt", "w")
outf.close()

numCases = int(inf.readline())
for w in range(0, numCases):

    indata = inf.readline()
    limits = indata.split()

    low = int(limits[0])
    high = int(limits[1])

    numSucc = 0
    for i in range(low, high):
        perm = i
        numDigits = str(i).__len__()
        for j in range(1,numDigits):
            
            strung = str(perm)
            if strung.__len__() == numDigits-1:
                strung = "0" + strung
            perm = int(strung[1:numDigits] + strung[0])
            
            if perm > i and low < perm <= high:
                numSucc += 1

    outf = open("recnumbers_out.txt", "a")
    outf.write("Case #" + str(w+1) + ": " + str(numSucc) + "\n")
    outf.close()

inf.close()
