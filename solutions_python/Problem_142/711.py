import sys
import itertools

def reducestring(instring):
    retstring = str()
    retstring += instring[0]
    count = 1
    while count <= len(instring) - 1:
        if instring[count-1] != instring[count]:
            retstring += instring[count]
        count += 1
    return retstring

##def reducetomatch(instring, matchstring):
##    retstring = str()
##    retstring += instring[0]
##    print "retstring", retstring
##    movecount = 0
##    count = 1
##    while count <= len(instring) - 1:
##        print "matchstring", matchstring[0:count+1]
##        if matchstring[0:count+1] == retstring + instring[count]:
##            retstring += instring[count]
##            print "retstring", retstring
##        else:
##            movecount += 1
##        count += 1
##    return movecount

# assume arrays are same size based on earlier checks
def changetomatch(instringarray, matchstringarray):
    count = 0
    matchmove = 0
    while count < len(instringarray):
        matchmove += abs(len(instringarray[count]) - len(matchstringarray[count]))
        count += 1
    return matchmove

def splitstring(instring, reducedstring):
    retarray = []
    reducedcount = 0
    stringcount = 0
    curstring = str()
    while stringcount < len(instring):
#        print reducedstring, instring, reducedcount, stringcount
        if instring[stringcount] != reducedstring[reducedcount]:
            retarray.append(curstring)
            curstring = str() + instring[stringcount]
            reducedcount += 1
        else:
            curstring += reducedstring[reducedcount]

        stringcount += 1
    retarray.append(curstring)
#    print retarray
    return retarray

filename = "A-small-attempt0.in"
outfilename = "A-small-attempt0.out"
if len(sys.argv) > 1:
    filename = sys.argv[1]
if len(sys.argv) > 2:
    outfilename = sys.argv[2]
inputfile = file(filename, 'rb')
outputfile = file(outfilename, 'wb')

case = 1

lines = inputfile.readlines()
testcases = int(lines[0].strip())
count = 1
case = 1
while count < len(lines):
    if len(lines[count].strip()) == 0:
        break
    numstrings = int(lines[count].strip().split(' ')[0])
    feglastrings = set()
#    print numstrings
    for num in range(0, numstrings):
        feglastrings.add(lines[count+num+1].strip())

    found = False
    if len(feglastrings) == 1:
        outputfile.write("Case #%i: 0\r\n" % case)
        print "Case #%i: 0" % case
        found = True

    omarstrings = set()
    for fegla in feglastrings:
        omarstrings.add(reducestring(fegla))
    if len(omarstrings) > 1:
        outputfile.write("Case #%i: Fegla won\r\n" % case) 
        print "Case #%i: Fegla won" % case
        found = True

    if found == False:
        minmoves = -1
        for feglastring in feglastrings:
            moves = 0
            for feglastring2 in feglastrings:
                if feglastring2 != feglastring:
#                    print reducestring(feglastring), reducestring(feglastring2)
#                    print splitstring(feglastring, reducestring(feglastring)), splitstring(feglastring2, reducestring(feglastring2))
                    moves += changetomatch(splitstring(feglastring, reducestring(feglastring)), splitstring(feglastring2, reducestring(feglastring2)))
            if (minmoves < 0) | (minmoves > moves):
                minmoves = moves
        moves = 0
        for feglastring in feglastrings:
            moves += changetomatch(splitstring(feglastring, reducestring(feglastring)), splitstring(reducestring(feglastring2), reducestring(feglastring2)))
        if (minmoves < 0) | (minmoves > moves):
            minmoves = moves

        outputfile.write("Case #%i: %i\r\n" % (case, minmoves))
        print "Case #%i: %i" % (case, minmoves)

    case += 1    
    count += numstrings + 1
    
inputfile.close()
outputfile.close()
