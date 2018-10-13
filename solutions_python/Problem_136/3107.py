PATH = r"C:\Users\Gil\Documents\jam\input2.txt"
OUTPATH = r"C:\Users\Gil\Documents\jam\output2.txt"

START_RATE = 2


def getTimeForNumberOfBuys(c,f,x,numberOfBuys):
    time = 0
    rate = START_RATE

    for i in range(numberOfBuys):
        time += (c / rate)
        rate += f

    return time + (x/rate)

def solveGame(data):
    c,f,x = data
    bestTime = 2**20

    numberOfBuys = 0

    while (True):
        
        tempTime = getTimeForNumberOfBuys(c,f,x,numberOfBuys)
        
        if tempTime >= bestTime:
            break
        else:
            bestTime = tempTime

        numberOfBuys += 1

    return str(bestTime)


data = open(PATH,"r").readlines()
data = [x.replace("\n","") for x in data]
data = [[float(i) for i in x.split(" ") ] for x in data]

numOfGames = int(data[0][0])

output = ""

for i in range(numOfGames):
    output += "Case #%s: " % (i+1)
    output += solveGame(data[1+i])
    output += "\n"

output = output.rstrip("\n")

print output
open(OUTPATH,"w").write(output)
