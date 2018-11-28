### Set the input and output file names
import time
import datetime
import string
import operator
from collections import defaultdict
filename = 'B-large'
input_filename = filename + '.in'
output_filename = filename + '.out.' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d-%H%M%S') + '.txt'


def multiCol(inputArr):
    #INITIALISE
    possible = True
    out = ""
    done = False
    mixR = "R"
    mixY = "Y"
    mixB = "B"
    vR  = inputArr[0]
    vRY = inputArr[1] # O
    vY  = inputArr[2]
    vYB = inputArr[3] # G
    vB  = inputArr[4]
    vRB = inputArr[5] # V
    
    #GREEN
    if vYB == 0:
        pass
    elif vR < vYB:
        possible = False
    elif vR == vYB and vYB > 0:
        if vRY + vY + vB + vRB > 0:
            possible = False
        else:
            mixR = "RG" * vR
            vR = 0
            vYB = 0
            out = mixR
    else:
        mixR = "RG" * vYB + "R"
        vR = vR - vYB
        vYB = 0

    #VIOLET
    if vRB == 0:
        pass
    elif vY < vRB:
        possible = False
    elif vY == vRB and vRB > 0:
        if vRY + vR + vB + vYB > 0:
            possible = False
        else:
            mixY = "YV" * vY
            vY = 0
            vRB = 0
            out = mixY
    else:
        mixY = "YV" * vRB + "Y"
        vY = vY - vRB
        vRB = 0
            
    #ORANGE
    if vRY == 0:
        pass
    elif vB < vRY:
        possible = False
    elif vB == vRY and vRY > 0:
        if vYB + vY + vR + vRB > 0:
            possible = False
        else:
            mixB = "BO" * vB
            vB = 0
            vRY = 0
            out = mixB
    else:
        mixB = "BO" * vRY + "B"
        vB = vB - vRY
        vRY = 0
    
    return (possible, out, mixR, mixY, mixB, vR, vY, vB)
#myA = [2, 0, 3, 1, 0, 0]   
#print(multiCol(myA))

   
def combineRYB(possible, out, firstR, firstY, firstB, vR, vY, vB):
    output = ""
    firstCol = ""
    lastCol = ""
    firstLoop = True
    if not(possible):
        output = "IMPOSSIBLE"
    elif out <> "":
        output = out
    else:
        while vR + vY + vB > 0:
            #INITIALISE
            if firstLoop:
                firstLoop = False
                if vR == max(vR, vY, vB):
                    if vR > vY + vB:
                        output = "IMPOSSIBLE"
                        break
                    else:
                        output = output + "R"
                        vR = vR - 1
                        firstCol = "R"
                        lastCol = "R"
                elif vY == max(vR, vY, vB):
                    if vY > vR + vB:
                        output = "IMPOSSIBLE"
                        break
                    else:
                        output = output + "Y"
                        vY = vY - 1
                        firstCol = "Y"
                        lastCol = "Y"
                elif vB == max(vR, vY, vB):
                    if vB > vR + vY:
                        output = "IMPOSSIBLE"
                        break
                    else:
                        output = output + "B"
                        vB = vB - 1
                        firstCol = "B"
                        lastCol = "B"
            else:
                if lastCol == "R":
                    if vY > vB:
                        output = output + "Y"
                        vY = vY - 1
                        lastCol = "Y"
                    elif vY < vB:
                        output = output + "B"
                        vB = vB - 1
                        lastCol = "B"
                    elif firstCol == "Y":
                        output = output + "Y"
                        vY = vY - 1
                        lastCol = "Y"
                    else:
                        output = output + "B"
                        vB = vB - 1
                        lastCol = "B"
                elif lastCol == "Y":
                    if vR > vB:
                        output = output + "R"
                        vR = vR - 1
                        lastCol = "R"
                    elif vR < vB:
                        output = output + "B"
                        vB = vB - 1
                        lastCol = "B"
                    elif firstCol == "R":
                        output = output + "R"
                        vR = vR - 1
                        lastCol = "R"
                    else:
                        output = output + "B"
                        vB = vB - 1
                        lastCol = "B"
                elif lastCol == "B":
                    if vR > vY:
                        output = output + "R"
                        vR = vR - 1
                        lastCol = "R"
                    elif vR < vY:
                        output = output + "Y"
                        vY = vY - 1
                        lastCol = "Y"
                    elif firstCol == "R":
                        output = output + "R"
                        vR = vR - 1
                        lastCol = "R"
                    else:
                        output = output + "Y"
                        vY = vY - 1
                        lastCol = "Y"
        if output <> "IMPOSSIBLE":
            if firstR <> "":
                output = output.replace("R",firstR,1)
            if firstY <> "":
                output = output.replace("Y",firstY,1)
            if firstB <> "":
                output = output.replace("B",firstB,1)
    return output
#print(combineRYB("xxx","yyy","zzz",200,30,50))
 

###### R  O  Y  G  B  V
#myA = [20, 10, 20, 10, 30, 10]
#myA = [0, 0, 2, 0, 0, 2]
#print(multiCol(myA))
#print(combineRYB(*[True, "R", "Y", "B", 10, 10, 19]))
#print(combineRYB(*multiCol(myA)))
    

### open input file for reading
with open(input_filename) as f:
    lines = f.read().splitlines()

    ### open output file for writing
    with open(output_filename, 'w') as output:

        ######################################################
        ### initialise variables from first line of the file
        ######################################################   
        vars = lines[0].split(' ')
        cases = int(vars[0])                    # number of cases
        print(str(cases) + ' cases detected.')  # [soft validation]
        linenum = 1                             # first case starts here
        casenum = 0                             # for counting the num of cases
        casesize_r = 1                          # number of rows in each case; default = 1
        casesize_c = 1                          # number of columns in each case; default = 1
        
        #infolines = True                        # toggle according to question
        infolines = False                       # toggle according to question
        
        ### i.e. infolines == true
        if infolines:
            pass
                
        ### i.e. infolines == false
        else:   
            for casenum in range(1, cases+1):
                #pass
                
                ### do the work!
                ### todo! 
                inputArr = lines[linenum].split(' ')
                inputArr = [ int(x) for x in inputArr ]

                myans = combineRYB(*multiCol(inputArr[1:]))
                
                linenum += 1
                
                ### output myans
                print('case #%d: %s\n' % (casenum, myans))
                output.write('case #%d: %s\n' % (casenum, myans))

                

### end
