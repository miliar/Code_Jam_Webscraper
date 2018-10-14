def addMote(arm):
    return arm * 2 - 1

def getMote(arm, x):
    times = 0
    while True:
        if arm > x:
            return (arm + x, times)
        else :
            arm = addMote(arm)
            times += 1

t = int(raw_input())
x = 0
while x < t:
    Armin, num = [int(l) for l in raw_input().split(" ")]

    mote = [int(l) for l in raw_input().split(" ")]

    if Armin == 1:
        print "Case #%d: %d" % (x+1, num)
    else :
        mote.sort() 

        while 0 < len(mote):
            if mote[0] < Armin:
                Armin += mote[0]
                mote.pop(0)
            else :
                break
    
        i = 0
        times = 0
        mini = False
        save = 0
        while i < len(mote):
            if mote[i] < Armin:
                Armin += mote[i]
            elif  mote[i] < Armin * 2 - 1:
                Armin = addMote(Armin)
                Armin += mote[i]
                times += 1
            else :
                mini = False
                adders = 0
                motes = 0
                save = len(mote) - i
                while i < len(mote):
                    Armin,adder = getMote(Armin, mote[i])
                    motes += 1
                    adders += adder
                    if adders <= motes:
                        mini = True
                        times += adders
                        break
                    i += 1
            i += 1
    
        if mini:
            print "Case #%d: %d" % (x+1, times)
        else:
            print "Case #%d: %d" % (x+1, times + save)
    x += 1
