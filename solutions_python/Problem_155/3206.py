rn = 0

def addAud(maxShyness, lst):
    global rn
    standingAud, origCount = 0, 0
    for i in range(0, maxShyness + 1):
        standingAud = lst[i] + standingAud
        origCount = lst[i] + origCount
        if standingAud > i + 1:
            pass
        else:
            while (i + 1) != standingAud:
                standingAud = standingAud + 1
    print ('Case #' + str(rn) + ': ' +  str(standingAud - origCount))

filename = '/Users/promisinganuj/Data/Technical/Python/standingovation.txt'
with open(filename) as f:
    for line in f:
        if rn == 0:
            pass
        else:
            maxShyness = int(line.split(' ')[0])
            lst = list(line.split(' ')[1].rstrip('\n'))
            lst = [int(i) for i in lst]
            addAud (maxShyness, lst)
        rn = rn + 1
f.close()