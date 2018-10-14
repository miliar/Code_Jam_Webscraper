# print ('Problem A: Standing Ovation')
filename = 'A-large.in'
numberOfLine = 0;
currentLine = 0;

def solve(data):
    addition = 0;
    accumulateStander = 0;
    indexOfSpace = data.index(' ')
    maxShy = int(data[:indexOfSpace])
    patron = data[indexOfSpace+1:]
    #print('patron: %s' % patron)
    for i, c in enumerate(patron):
        #print('%d > %d + %d' % (i, accumulateStander, addition))
        while i > accumulateStander + addition:
            #print('Add one person')
            addition += 1

        accumulateStander += int(c)
    print('Case #%d: %d' % (currentLine, addition))
    # print('maxShy %d -%s' % (maxShy, patron))

def answer(data):
    solve(data);
    #print ('line %d: %s' % (currentLine, data))

with open(filename) as fi:

    lines = fi.read().splitlines()

    for data in lines:
        if numberOfLine != 0:
            currentLine += 1
            answer(data)
        else:
            numberOfLine = data

    #print('number of line ' + numberOfLine)
