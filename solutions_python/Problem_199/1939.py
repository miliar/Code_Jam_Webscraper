class MyString:
    def __init__ (self, string, parent):
        self.string = string
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__ (self, other):
        if (self.string == other.string):
            return True
        else:
            return False

def heuristic(string):
    i = 0
    for c in string.string:
        if c == '-':
            i += 1
    return i

def popFromOpenSet(openSet):
    minVal = 0
    for i in range(len(openSet)):
        if (openSet[i].f < openSet[minVal].f):
            minVal = i
        if (openSet[i].f == openSet[minVal].f):
            if (openSet[i].g > openSet[minVal].g):
                        minVal = i
    cell = openSet[minVal]
    del openSet[minVal]
    return cell

def getNeighbours(current, k):
    neighbors = []
    for i in range(len(current.string) - k + 1):
        newString = current.string[:]
        for j in range(k):
            if (newString[i+j] == '+'):
                newString[i+j] = '-'
            else:
                newString[i+j] = '+'
        # print ("neighbour", newString)
        neighbors.append(MyString(newString, current))
    return neighbors

tc = int(input())

for etc in range(tc):

    startString, k = input().strip().split()
    k = int (k)
    goalString = '+' * len(startString)



    start = MyString(list(startString), None)
    goal = MyString(list(goalString), None)

    openSet = []
    closedSet = []

    openSet.append(start)

    while (len(openSet) > 0):
        current = popFromOpenSet(openSet)

        # print (current.string)

        if(current == goal):
            break

        closedSet.append(current)

        neighbors = getNeighbours(current, k)
        for neighbor in neighbors:
            if(neighbor not in closedSet):

                tempG = current.g + 1

                if (neighbor not in openSet):
                    openSet.append(neighbor)
                else:
                    if (tempG >= neighbor.g):
                        continue

                neighbor.g = tempG
                neighbor.f = neighbor.g + heuristic(neighbor)

    if (current == goal):
        print ("Case #" + str(etc + 1) + ": " + str(current.g))
    else:
        print ("Case #" + str(etc + 1) + ": " + "IMPOSSIBLE")
