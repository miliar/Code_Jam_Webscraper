from sys import argv

def solveProblem(fin, fout):
    tcCount = int(fin.readline())
    opTCCount = 1
    tcList = []
    isPlayLeft = False
    isCompleted = False
    jumptoNextTC = False
    for i in range(tcCount*4+tcCount):
        str = fin.readline()
        if str.strip():
            if jumptoNextTC: continue
            playList = []
            xcount = 0
            ocount = 0
            for play in str.strip():
                playList.append(play)
                if play=='.': isPlayLeft = True
                if play=='X': xcount+=1
                if play=='O': ocount+=1
                if play=='T': 
                    xcount+=1
                    ocount+=1
            if xcount==4:
                fout.write("Case #%s: %s\n" % (opTCCount, "X won"))
                opTCCount+=1
                jumptoNextTC = True
            if ocount==4:
                fout.write("Case #%s: %s\n" % (opTCCount, "O won"))
                opTCCount+=1
                jumptoNextTC = True
            tcList.append(playList)
        else:
            if jumptoNextTC:
                jumptoNextTC = False
                tcList = []
                continue
            print tcList
            for i in range(4):
                xcount = 0
                ocount = 0
                for row in tcList:
                    if row[i]=='X': xcount+=1
                    if row[i]=='O': ocount+=1
                    if row[i]=='T': 
                        xcount+=1
                        ocount+=1
                if xcount==4:
                    fout.write("Case #%s: %s\n" % (opTCCount, "X won"))
                    opTCCount+=1
                    isCompleted = True
                    break
                if ocount==4:
                    fout.write("Case #%s: %s\n" % (opTCCount, "O won"))
                    opTCCount+=1
                    isCompleted = True
                    break
            if not isCompleted:
                xcount_d1 = 0
                ocount_d1 = 0
                xcount_d2 = 0
                ocount_d2 = 0                
                for row,col in enumerate(tcList):
                    print col[row]
                    if col[row]=='X': xcount_d1+=1
                    if col[row]=='O': ocount_d1+=1
                    if col[row]=='T':
                        xcount_d1+=1
                        ocount_d1+=1
                    if col[3-row]=='X': xcount_d2+=1
                    if col[3-row]=='O': ocount_d2+=1
                    if col[3-row]=='T':
                        xcount_d2+=1
                        ocount_d2+=1
                if xcount_d1==4:
                    fout.write("Case #%s: %s\n" % (opTCCount, "X won"))
                    opTCCount+=1
                    isCompleted = True
                if ocount_d1==4:
                    fout.write("Case #%s: %s\n" % (opTCCount, "O won"))
                    opTCCount+=1
                    isCompleted = True
                if xcount_d2==4:
                    fout.write("Case #%s: %s\n" % (opTCCount, "X won"))
                    opTCCount+=1
                    isCompleted = True
                if ocount_d2==4:
                    fout.write("Case #%s: %s\n" % (opTCCount, "O won"))
                    opTCCount+=1
                    isCompleted = True                    
            if isPlayLeft and not isCompleted:
                fout.write("Case #%s: %s\n" % (opTCCount, "Game has not completed"))
                opTCCount+=1                
            if not isPlayLeft:
                fout.write("Case #%s: %s\n" % (opTCCount, "Draw"))
                opTCCount+=1
            isPlayLeft = False
            isCompleted = False
            tcList = []

solveProblem(open(argv[1]), open(argv[1].replace("in", "out"), "w"))