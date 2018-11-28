def readInput():
    inFileName = "A-large.in"
    
    f = open(inFileName)
    for line in f.readlines():
        line = line.rstrip("\r\n")
        yield line
    f.close()

        
inputGen = readInput()

currentNumber = 1
wholeNumber = int( inputGen.next() )
while True:
    try:
        [N, K] = [int(x) for x in inputGen.next().split(" ")]
        onoff = 2 ** N - (K % (2 ** N))
        if onoff == 1:
            output = "ON"
        else:
            output = "OFF"
        print "Case #%d: %s" % (currentNumber, output)
        currentNumber += 1
    except StopIteration:
        break
    