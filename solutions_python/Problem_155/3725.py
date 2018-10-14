def standingOvation(cNr, mSLvl, iNr):
    caseNr = cNr
    count = mSLvl+1
    inputNr = iNr
    standing = 0 # at the beginning no one stands
    currShyLvl = 0
    friendsToAdd = 0
    while len(inputNr) > 0:
        audience = int(inputNr[0])
        if audience > 0: # if anyone wants to stand up
            if standing < currShyLvl: # check if enough people are standing
                friendsToAdd += currShyLvl - standing
                standing += friendsToAdd
                #print("standing: %i" % standing)
                #print("currShyLvl: %i" % currShyLvl)
                #print("friendsToAdd: %i" % friendsToAdd)
            standing += audience # audience at this shyness lvl stand up
        inputNr = inputNr[1:]
        currShyLvl += 1
    return "Case #%i: %i" %(caseNr, friendsToAdd)


def main():
    with open("./A-small-attempt1.in") as f:
        lines = f.readlines()
        c = int(lines[0])
        for i in range(1,c+1):
            l = lines[i]
            mSLvl, iNr = l.split(" ")
            iNr = iNr.split("\n")[0]
            print(standingOvation(i, int(mSLvl), iNr))

main()
            
