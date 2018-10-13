import math
def FnS():
    cases = 0
    inp = open('test.txt', 'r')
    testC = inp.readline()
    f = open('op3.txt','w')
    if int(testC)>= 1 and int(testC) <= 100:
        for i in range(int(testC)):
            cases += 1
            counter = 0
            CaseX = inp.readline()
            CaseS = CaseX.split()
            lowLim = int(CaseS[0])
            upLim = int(CaseS[1])
            if (lowLim and upLim) >= 1 and (lowLim and upLim) <= 1000:
                for i in range(lowLim, upLim+1):
                    if str(i) == str(i)[::-1]:
                        SqI = math.sqrt(i)
                        if (SqI-int(SqI)) == 0 and str(int(SqI)) == str(int(SqI))[::-1]:
                            counter += 1
            f.write('Case #' + str(cases) + ': ' + str(counter) + '\n')
FnS()
