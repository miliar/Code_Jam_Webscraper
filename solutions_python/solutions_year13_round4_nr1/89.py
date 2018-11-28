problemName = "A-large (2)"
#problemName = "test"

class multiQueue(object):
    def __init__(self):
        self.que = []
        
    def push(self, station, people):
        self.que.append((station, people))
        
    def pop(self, stationOff, people,costFunc):
        Runningcost = 0
        while people > 0:
            stationOn, peopleOff = self.que.pop()
            people -= peopleOff
            if people < 0:
                peopleOff += people
                self.push(stationOn, -1 * people)
            Runningcost += costFunc((stationOn, stationOff, peopleOff))
        return Runningcost

def cost(totalStops):
    def cost2((start, end, num)):
        dist = end - start
        return num * (dist * totalStops - (pow(dist - 1,2) + dist - 1) / 2)
    return cost2
        
# def cost(totalStops):
    # totalCost = ( pow(totalStops, 2) + totalStops ) / 2
    # def cost2((start, end, num)):
        # missedStops = totalStops - (end - start)
        # perCost = (pow(missedStops, 2) + missedStops) / 2
        # perCost = totalCost - perCost
        # return perCost * num
    # return cost2

ENTER = 0
EXIT = 1
    
def solve():
    numStops, numJournys = next(int, True)
    costFunc = cost(numStops)
    
    journys = [ next(int, True) for i in xrange(0,numJournys) ]
    #journys = map(lambda a: (a[0] -1, a[1] -1, a[2]), journys)
    
    proposedProfit = sum(map(costFunc, journys))
    simulation = multiQueue()
    
    events = sorted( [(i[0], ENTER, i[2]) for i in journys] + [(i[1], EXIT, i[2]) for i in journys])
    actualProfit = 0
    for i in events:
        if i[1] == ENTER:
            simulation.push(i[0], i[2])
        else:
            actualProfit += simulation.pop(i[0], i[2], costFunc)
    answer = (proposedProfit - actualProfit) % 1000002013
    return answer


fin = open( problemName + ".in", "r")
fout = open( problemName + ".out", "w")


def next(conversionFunc, split = False):
    if split:
        return map(conversionFunc, fin.readline().strip().split(" ") )
    else:
        return conversionFunc( fin.readline().strip() )
    
for case in xrange(1, next(int) + 1):
    print case
    fout.write("Case #" + str(case) + ": ")

    fout.write(str(solve()))
    
    fout.write('\n')

fin.close()
fout.close()