def loadWords():
    inFile = open('B-small-attempt0.in', 'r', 0)
    line = inFile.readlines()
    numLines = line.pop(0)
    line = [x.strip('\n') for x in line]
    temp = []
    for i in line:
        temp.append(i)
    return temp, int(numLines)

def writeWords(lst):
    out = open('B-small-attempt0.out', 'w')
    count = 0
    for i in lst:
        count +=1
        out.write('Case #%d: ' %count + str(i) +'\n')
        
load, number = loadWords()

for_print = []
for game in load:
    game = [float(x) for x in game.split(' ')]
    start = 2.0
    farm = game[0]
    farmGain = game[1]
    goal = game[2]
    
    
    farm_time = 0
    while True:
        notFarm = goal/start
        withFarm = farm/start + goal/(start + farmGain)
        if notFarm < withFarm: 
            for_print.append(goal/start + farm_time)
            break
        else:
            farm_time += farm/start
            start += farmGain
writeWords(for_print)