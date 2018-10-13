file = open("C-small-1-attempt0.in", "r")
ofile = open("output.txt", "w")
intCases = int(file.readline()[:-1])
for i in range(intCases):
    inputs = file.readline()[:-1].split()
    stalls = [j for j in range(int(inputs[0]))]
    superStalls = []
    superStalls.append(stalls)
    for j in range(int(inputs[-1])):
        currentStalls = max(superStalls)
        stallsLength = len(currentStalls)
        if stallsLength % 2 == 1:
            firstStalls = [k for k in range(int((stallsLength-1)/2))]
            secondStalls = [k for k in range(int((stallsLength-1)/2))]
        else:
            firstStalls = [k for k in range(int(stallsLength/2)-1)]
            secondStalls = [k for k in range(int(stallsLength/2))]
        superStalls.remove(currentStalls)
        superStalls.append(firstStalls)
        superStalls.append(secondStalls)
    ofile.write("Case #" + str(i+1) + ": " + str(len(secondStalls)) + " " + str(len(firstStalls)) + "\n")
ofile.close()            
