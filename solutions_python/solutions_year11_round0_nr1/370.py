import sys

def main():
    f = open(sys.argv[1])
    noOfCases = int(f.readline())
    lines = f.readlines()
    for i, l in zip(range(1, len(lines) + 1), lines):
        print "Case #%d: %d" % (i, solveCase(l))

def solveCase(line):
    xs = line.split()
    noOfButtons = int(xs[0])
    xs = xs[1:]
    colours = {"O":(1, 0), "B":(1, 0)}
    lastPushTime = 0
    for i in xrange(noOfButtons) :
        colour, button = xs[i * 2], int(xs[i*2+1])
        lastButton, lastTime = colours[colour]
        pressTime = lastTime + abs(button - lastButton) + 1
        if pressTime <= lastPushTime:
            pressTime = lastPushTime + 1
        lastPushTime = pressTime
        #print colour, pressTime
        colours[colour] = (button, pressTime)
    return lastPushTime

main()


