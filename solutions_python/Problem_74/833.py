from formatFile import *
cases = formatFile('Bot Trust.txt', 1, True)

answers = []

for case in cases:
    tempcase = case[0].split()
    caseNum = tempcase.pop(0)
    case = []
    tempbutton = []
    for a in xrange(len(tempcase)/2):
        for i in xrange(2):
            tempbutton.append(tempcase.pop(0))
        case.append(tempbutton)
        tempbutton = []
    oPosition = 1
    bPosition = 1
    oList = []
    bList = []
    oNextPos = 1
    bNextPos = 1
    oFinished = False
    bFinished = False
    pressed = 0
    time = 0
    for i in xrange(len(case)):
        if case[i][0] == 'B':
            bList.append([int(case[i][1]), i])
        else:
            oList.append([int(case[i][1]), i])
    if oList:
        oNextPos = oList[0]
        oList.pop(0)
    else:
        oFinished = True
    if bList:
        bNextPos = bList[0]
        bList.pop(0)
    else:
        bFinished = True
    print 'hello'
    print case
    print oList
    for i in xrange(int(caseNum)):
        while pressed < i + 1:
            noPress = False
            if not bFinished:
                if bPosition < bNextPos[0]:
                    bPosition += 1
                elif bPosition > bNextPos[0]:
                    bPosition -= 1
                else:
                    if pressed == bNextPos[1]:
                        pressed += 1
                        noPress = True
                        if bList:
                            bNextPos = bList[0]
                            bList.pop(0)
                        else:
                            bFinished = True
                            
            if not oFinished:
                if oPosition < oNextPos[0]:
                    oPosition += 1
                elif oPosition > oNextPos[0]:
                    oPosition -= 1
                else:
                    if not noPress:
                        if pressed == oNextPos[1]:
                            pressed += 1
                            if oList:
                                oNextPos = oList[0]
                                oList.pop(0)
                            else:
                                oFinished = True
            if pressed == caseNum:
                break
            time += 1
    answers.append(time)
     
createAnswer(answers, 'Bot Trust Answers.txt')
print 'Done'
