import sys

def solveSequence(line):
    tok = line.split(' ')
    seqLen = int(tok[0])
    OPos = 1
    BPos = 1
    OBotTime = 0
    BBotTime = 0
    totalTime = 0
    lastBot = tok[1]
    for i in range(seqLen):
        bot = tok[i*2+1]
        butt = int(tok[i*2+2])
        turnChange = bot != lastBot
        if bot == 'O':
            if turnChange:
                totalTime = totalTime + BBotTime
                OBotTime = abs(butt-OPos) + 1 - BBotTime
                if OBotTime < 1:
                    OBotTime = 1
                BBotTime = 0
            else:
                OBotTime = OBotTime + abs(butt-OPos) + 1
            OPos = butt
        else:
            if turnChange:
                totalTime = totalTime + OBotTime
                BBotTime = abs(butt-BPos) + 1 - OBotTime
                if BBotTime < 1:
                    BBotTime = 1
                OBotTime = 0
            else:
                BBotTime = BBotTime + abs(butt-BPos) + 1
            BPos = butt
        lastBot = bot
    return totalTime+BBotTime+OBotTime
        

if len(sys.argv) > 1:
    f = open(sys.argv[1],'r')
    lines = f.read().split('\n');
    nCases = int(lines[0])
    for i in range(1,nCases+1):
        print 'Case #%d: %s' % (i,solveSequence(lines[i]))
    f.close()
else:
    print "uso: "+sys.argv[0]+" <input-file>"  