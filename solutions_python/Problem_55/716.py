
import sys, collections

class RollerCoaster:
    
    def __init__(self, size):
        self.capacity = size
        self.riders = []
        
    def boardGroup(self, group):
        if sum(self.riders) + group > self.capacity:
            return False
        else:
            self.riders.append(group)
            return True

def rollerCoasterProfit(rides, size, groups):
    
    euros = 0
    coaster = RollerCoaster(size)
    groupQueue = collections.deque(groups)
    
    for ride in range(rides):
        while len(groupQueue) > 0 and coaster.boardGroup(groupQueue[0]):
            euros = euros + groupQueue.popleft()
        groupQueue.extend(coaster.riders)
        coaster.riders = []
        
    return euros

if len(sys.argv) > 1:
    input = open(sys.argv[1])
else:
    input = open(raw_input("input file: "))
    
cases = int(input.readline())

for case in range(1, cases + 1):
    rcString = input.readline()
    rcArgs = map(int, rcString.split(" "))
    
    groupString = input.readline()
    groupList =  map(int, groupString.split(" "))
    
    print "Case #%i: %i" % (case, rollerCoasterProfit(rcArgs[0], rcArgs[1], groupList))