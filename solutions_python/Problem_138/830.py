inputFile = open("D-large.in", "r")
outputFile = open("D-large.out", "w")

testCases = int(inputFile.readline())
caseNumber = 1

for length in range(testCases):
    testCaseLen = int(inputFile.readline())

    decietPoints = 0
    truthPoints = 0
    
    naomi = []
    ken = []

    naomiHit = []
    kenHit = []
    
    for val in range(2):
        inputLine = inputFile.readline().split()
        for char in range(testCaseLen):
            inputLine[char] = float(inputLine[char])
                
            if val == 0:
                naomi.append(inputLine[char])
            elif val == 1:
                ken.append(inputLine[char])

    naomi.sort()
    ken.sort()
    
    while(len(naomi) !=0 and len(ken) !=0):
        if naomi[-1] > ken[-1]:
            decietPoints += 1

            naomiHit.append(naomi[-1])
            naomi.pop(-1)

            kenHit.append(ken[-1])
            ken.pop(-1)
        elif naomi[-1] < ken[-1]:
            naomiHit.append(naomi[0])
            naomi.pop(0)

            kenHit.append(ken[-1])
            ken.pop(-1)

    naomi = naomiHit
    ken = kenHit

    naomi.sort()
    ken.sort()

    noamiHit = []
    kenHit = []

    for val in range(len(naomi)):
        hit = False
        
        for null in range(len(ken)):
            if naomi[0] > ken[null]:
                pass
            elif naomi[0] < ken[null]:
                naomiHit.append(naomi[0])
                naomi.pop(0)

                kenHit.append(ken[null])
                ken.pop(null)
                hit = True
                break

        if hit != True:
            truthPoints += 1
            naomiHit.append(naomi[0])
            naomi.pop(0)

            kenHit.append(ken[0])
            kenHit.pop(0)
        
    outputFile.write("Case #" + str(caseNumber) + ": " + str(decietPoints) + " " + str(truthPoints) + "\n")

    caseNumber += 1
            
inputFile.close()
outputFile.close()
