import sys

###############################################################################
# Helper functions                                                            #
###############################################################################
def parseInput(input):
    case = []    
    # PARSE INPUT

    return case

def handleCase(case):
    res = []

    base = len(set(case))
    if base < 2:
        base = 2

    interp = {case[0]:1}
    curVal = 0
    for c in case[1:]:
        if not c in interp:
            if curVal == 0:
                interp[c] = 0
                curVal = 2
            else:
                interp[c] = curVal
                curVal += 1
    res = ''
    for c in case:
        res += str(interp[c])        

    res = int(res,base)            

    return res

###############################################################################
# Main                                                                        #
###############################################################################

input  = open(sys.argv[1])
output = open(sys.argv[1].replace('in','out'),'w')
#debug  = open(sys.argv[1].replace('in','debug'),'w')

nCases = int(input.readline().strip())

for i in range(nCases):
    # case = parseInput(input)
    case = input.readline().strip()    

    res = handleCase(case)   

    print "Case #" + str(i+1) + ": " + case + "\t" + str(res)
    output.write('Case #' + str(i+1) + ": " + str(res) + '\r\n')
