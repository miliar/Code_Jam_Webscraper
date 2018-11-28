def main():
    inputfile = open("A-large.in", "r")
    outputfile = open("output", "w")
    currentcase = 1
    inputfile.readline()
    for line in inputfile:
        linelist = line.strip().split()[1:]
        index = 0
        blue = {}
        orange = {}
        length = len(linelist)
        while index < length:
            if linelist[index] == 'O':
                orange[index/2] = int(linelist[index + 1])
                index += 1
            elif linelist[index] == 'B':
                blue[index/2] = int(linelist[index + 1])
                index += 1
            index += 1
        bluekeys = blue.keys()
        orangekeys = orange.keys()
        bluekeys.sort()
        orangekeys.sort()
        bluelen = len(bluekeys)
        orangelen = len(orangekeys)
        bcur = 0
        ocur = 0
        opos = 1
        bpos = 1
        totalstep = 0
        length = length/2
        for i in xrange(0, length):
            if i in bluekeys:
                nextbpos = blue[i]
                step = abs(nextbpos - bpos) + 1
                bpos = nextbpos
                bcur = bluekeys.index(i) + 1
                if orangelen and ocur < orangelen:
                    nextopos = orange[orangekeys[ocur]]
                    if abs(nextopos - opos) > (step - 1):
                        if nextopos - opos < 0:
                            opos -= step 
                        else:
                            opos += step 
                    else:
                        opos = nextopos
            else:
                nextopos = orange[i]
                step = abs(nextopos - opos) + 1
                opos = nextopos
                ocur = orangekeys.index(i) + 1
                if bluelen and bcur < bluelen:
                    nextbpos = blue[bluekeys[bcur]]
                    if abs(nextbpos - bpos) > (step - 1):
                        if nextbpos - bpos < 0:
                            bpos -= step 
                        else:
                            bpos += step  
                    else:
                        bpos = nextbpos
            totalstep += step
        output = "Case #%d: %d\n" % (currentcase, totalstep)
        outputfile.write(output)
        currentcase += 1
    
    inputfile.close()
    outputfile.close()
    
if __name__ == "__main__":
    main()