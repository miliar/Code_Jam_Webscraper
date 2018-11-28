import sys

inFile = open(sys.argv[1], 'r')

outFile = open(sys.argv[1][:-2]+"out", "w")

number_of_input = int(inFile.readline().rstrip("\n"))
#print number_of_input

count = 0
while(count != number_of_input):
    matrix = []
    for line in range(0,4):
        attrib = inFile.readline().rstrip("\n")
        attrib = list(attrib)
        matrix.append(attrib)

    inFile.readline().rstrip("\n")
    count = count + 1
    
    rTest = 0;
    cTest = 0;
    LRTest = 0;
    RLTest = 0;
    draw = 0;
    dot = 0;
    who = ""
    diagTest = 0;


    for i in range(0,1):

        LR = ""
        RL = ""
        for j in range(0,4):
            LR = LR + matrix[j][j]
            RL = RL + matrix[j][3-j]


        xLRCount = LR.count("X")
        oLRCount = LR.count("O")

        xRLCount = RL.count("X")
        oRLCount = RL.count("O")


        if(xLRCount >= 3):
            if(xLRCount == 4):
                won = "X"
                #print "Case #%d: %c won" %(count, won)
                outFile.write("Case #%d: %c won\n" %(count, won))
                diagTest = 1
                break;
            else:
                if(("O" not in LR) and ("." not in LR) and ("T" in LR)):
                    won = "X"
                    #print "Case #%d: %c won" %(count, won)
                    outFile.write("Case #%d: %c won\n" %(count, won))
                    diagTest = 1
                    break;


        if(oLRCount >= 3):
            if(oLRCount == 4):
                won = "O"
                #print "Case #%d: %c won" %(count, won)
                outFile.write("Case #%d: %c won\n" %(count, won))
                diagTest = 1
                break;
            else:
                if(("X" not in LR) and ("." not in LR) and ("T" in LR)):
                    won = "O"
                    #print "Case #%d: %c won" %(count, won)
                    outFile.write("Case #%d: %c won\n" %(count, won))
                    diagTest = 1
                    break;


        if(xRLCount >= 3):
            if(xRLCount == 4):
                won = "X"
                #print "Case #%d: %c won" %(count, won)
                outFile.write("Case #%d: %c won\n" %(count, won))
                diagTest = 1
                break;
            else:
                if(("O" not in RL) and ("." not in RL) and ("T" in RL)):
                    won = "X"
                    #print "Case #%d: %c won" %(count, won)
                    outFile.write("Case #%d: %c won\n" %(count, won))
                    diagTest = 1
                    break;


        if(oRLCount >= 3):
            if(oRLCount == 4):
                won = "O"
                #print "Case #%d: %c won" %(count, won)
                outFile.write("Case #%d: %c won\n" %(count, won))
                diagTest = 1
                break;
            else:
                if(("X" not in RL) and ("." not in RL) and ("T" in RL)):
                    won = "O"
                    #print "Case #%d: %c won" %(count, won)
                    outFile.write("Case #%d: %c won\n" %(count, won))
                    diagTest = 1
                    break;

    if(diagTest == 0):
        ##print "Continue"
        for r in range(0,4):
            LR = ""
            TB = ""
            for c in range(0,4):
                LR = LR + matrix[r][c]
                TB = TB + matrix[c][r]


            xLRCount = LR.count("X")
            oLRCount = LR.count("O")
            
            xTBCount = TB.count("X")
            oTBCount = TB.count("O")


            if(xLRCount >= 3):
                if(xLRCount == 4):
                    won = "X"
                    #print "Case #%d: %c won" %(count, won)
                    outFile.write("Case #%d: %c won\n" %(count, won))
                    rTest = 1
                    break;
                else:
                    if(("O" not in LR) and ("." not in LR) and ("T" in LR)):
                        won = "X"
                        #print "Case #%d: %c won" %(count, won)
                        outFile.write("Case #%d: %c won\n" %(count, won))
                        rTest = 1
                        break;


            if(oLRCount >= 3):
                if(oLRCount == 4):
                    won = "O"
                    #print "Case #%d: %c won" %(count, won)
                    outFile.write("Case #%d: %c won\n" %(count, won))
                    rTest = 1
                    break;
                else:
                    if(("X" not in LR) and ("." not in LR) and ("T" in LR)):
                        won = "O"
                        #print "Case #%d: %c won" %(count, won)
                        outFile.write("Case #%d: %c won\n" %(count, won))
                        rTest = 1
                        break;


            if(xTBCount >= 3):
                if(xTBCount == 4):
                    won = "X"
                    #print "Case #%d: %c won" %(count, won)
                    outFile.write("Case #%d: %c won\n" %(count, won))
                    cTest = 1
                    break;
                else:
                    if(("O" not in TB) and ("." not in TB) and ("T" in TB)):
                        won = "X"
                        #print "Case #%d: %c won" %(count, won)
                        outFile.write("Case #%d: %c won\n" %(count, won))
                        cTest = 1
                        break;


            if(oTBCount >= 3):
                if(oTBCount == 4):
                    won = "O"
                    #print "Case #%d: %c won" %(count, won)
                    outFile.write("Case #%d: %c won\n" %(count, won))
                    cTest = 1
                    break;
                else:
                    if(("X" not in TB) and ("." not in TB) and ("T" in TB)):
                        won = "O"
                        #print "Case #%d: %c won" %(count, won)
                        outFile.write("Case #%d: %c won\n" %(count, won))
                        cTest = 1
                        break;
    
    
        if(cTest == 0 and rTest == 0):
            for r in range(0,4):
                for c in range(0,4):
                    if(matrix[r][c] == "."):
                        dot = dot + 1

            if(dot > 0):
                #print "Case #%d: Game has not completed" %(count)
                outFile.write("Case #%d: Game has not completed\n" %(count))
            else:
                #print "Case #%d: Draw" %(count)
                outFile.write("Case #%d: Draw\n" %(count))
