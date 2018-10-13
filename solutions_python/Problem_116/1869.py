import glob, os, math

def wtf():

    # output file
    h= open('output.txt','w+')

    caseNumber= 1
    coco= 0
    with open('input.txt','r') as f:
        stringy= ""
        for line in f.readlines():
            if (coco == 0):
                coco=1
            else:
                me= line
                if (len(me) == 1):
                    answer= isPalin(stringy)
                    h.write("Case #" + str(caseNumber) + ": " + answer + "\n")
                    stringy=""
                    caseNumber += 1
                else:
                    stringy=stringy + me.strip()
        
    f.close()
            


def isPalin(stringer):

    sumx= 0
    sumo= 0

    #rows
    rone=[0,1,2,3]
    rtwo=[4,5,6,7]
    rthree=[8,9,10,11]
    rfour=[12,13,14,15]

    for l in xrange(4):
        sumx += int(me(stringer[rone[l]])[0])
        sumo += int(me(stringer[rone[l]])[1])


    if answer(sumx,sumo) is not "":
        return answer(sumx,sumo)

    sumx= 0
    sumo= 0

    for l in xrange(4):
        sumx += int(me(stringer[rtwo[l]])[0])
        sumo += int(me(stringer[rtwo[l]])[1])

    if answer(sumx,sumo) is not "":
        return answer(sumx,sumo)

    sumx= 0
    sumo= 0

    for l in xrange(4):
        sumx += int(me(stringer[rthree[l]])[0])
        sumo += int(me(stringer[rthree[l]])[1])

    if answer(sumx,sumo) is not "":
        return answer(sumx,sumo)

    sumx= 0
    sumo= 0

    for l in xrange(4):
        sumx += int(me(stringer[rfour[l]])[0])
        sumo += int(me(stringer[rfour[l]])[1])

    if answer(sumx,sumo) is not "":
        return answer(sumx,sumo)

    sumx= 0
    sumo= 0
    
    

    #columns
    cone=[0,4,8,12]
    ctwo=[1,5,9,13]
    cthree=[2,6,10,14]
    cfour=[3,7,11,15]
    
    for l in xrange(4):
        sumx += int(me(stringer[cone[l]])[0])
        sumo += int(me(stringer[cone[l]])[1])

    if answer(sumx,sumo) is not "":
        return answer(sumx,sumo)

    sumx= 0
    sumo= 0

    for l in xrange(4):
        sumx += int(me(stringer[ctwo[l]])[0])
        sumo += int(me(stringer[ctwo[l]])[1])

    if answer(sumx,sumo) is not "":
        return answer(sumx,sumo)

    sumx= 0
    sumo= 0

    for l in xrange(4):
        sumx += int(me(stringer[cthree[l]])[0])
        sumo += int(me(stringer[cthree[l]])[1])

    if answer(sumx,sumo) is not "":
        return answer(sumx,sumo)

    sumx= 0
    sumo= 0
    
    for l in xrange(4):
        sumx += int(me(stringer[cfour[l]])[0])
        sumo += int(me(stringer[cfour[l]])[1])

    if answer(sumx,sumo) is not "":
        return answer(sumx,sumo)


    sumx = 0
    sumo = 0
    may= [0,5,10,15]
    be= [3,6,9,12]
    for l in xrange(4):
        sumx += int(me(stringer[may[l]])[0])
        sumo += int(me(stringer[may[l]])[1])

    if answer(sumx,sumo) is not "":
        return answer(sumx,sumo)

    sumx= 0
    sumo= 0

    for ff in xrange(4):
        sumx += int(me(stringer[be[ff]])[0])
        sumo += int(me(stringer[be[ff]])[1])

    if answer(sumx,sumo) is not "":
        return answer(sumx,sumo)

    sumx= 0
    sumo= 0

    if "." in stringer:
        return "Game has not completed"
    else:
        return "Draw"



    
            

def answer(a,b):
    if (a == 4):
        return "X won"
    elif (b == 4):
        return "O won"
    else:
        return ""
        


    
    

def me(part):
    if part == "X":
        return [1,0]
    elif part == "O":
        return [0,1]
    elif part == "T":
        return [1,1]
    else:
        return [0,0]
    return [x,o]
            

    
    
