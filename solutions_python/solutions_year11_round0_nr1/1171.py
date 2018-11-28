currentPosition = 0
Position = {}
inData = None
outData = None

currentPosition = 0

class Input:
    def __init__(self, line, i):
        points = line.split(' ')
        self.buttons = []
        self.Num = i
        self.steps = int ( points[0] )
        for x in points[1:]:
            if x == 'O':
                color = 'O'
            elif x == 'B':
                color = 'B'
            else:
                self.buttons.append( [color, int(x)] )
class Output:
    def __init__(self):
        self.res = 0
    def dump(self, outFile):
        outFile.write("Case #%d: %d\n" % (self.Num, self.res))

def getNext(nextPosition):
    global currentPosition

    O = [x for x in inData.buttons[currentPosition:]if x[0] == 'O']
    if len(O) != 0:
        nextPosition['O'] = O[0][1]

    B = [x for x in inData.buttons[currentPosition:]if x[0] == 'B']
    if len(B) != 0:
        nextPosition['B'] = B[0][1]

    if inData.buttons[currentPosition][0] == 'O':
        first, second = 'O', 'B'

    else:
        first, second = 'B', 'O'

    currentPosition += 1

    return first, second, nextPosition

def solve(inData):
    global Position

    output = Output()
    output.Num = inData.Num

    Position = { 'O': 1, 'B': 1 }
    nextPosition = { 'O': 1, 'B': 1 }

    for i in range(0, inData.steps):

        first, second, nextPosition = getNext(nextPosition)

        step = { 'O' : abs(nextPosition['O'] - Position['O']),
                 'B' : abs(nextPosition['B'] - Position['B']) }

        step[first] += 1

        Position[first] = nextPosition[first]
        output.res += step[first]

        if step[second] <= step[first]:
            Position[second] = nextPosition[second]
        else:
            if (nextPosition[second] > Position[second]):
                Position[second] += step[first]
            else:
                Position[second] -= step[first]


    return output

def main():
    global currentPosition
    inputF = open("input.txt", "r")
    outputF = open("out", "w")
    N = int( inputF.readline() )
    for i in range(1, N + 1):
        line = inputF.readline()
        global inData
        global outData

        currentPosition = 0
        inData = Input(line, i)
        outData = solve(inData)
        outData.dump(outputF)

        i += 1
    inputF.close()
    outputF.close()
    return

main()