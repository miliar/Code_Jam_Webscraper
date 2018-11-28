import sys

###############################################################################
# Helper functions                                                            #
###############################################################################
def handleCase(case):
    case.insert(0,0)
    for i in range(len(case)-1,-1,-1):
        iter2 = range(i,len(case))
        iter2.reverse()
        for j in iter2:
            if(case[i] < case[j]):
                result = case[:]
                result[i] = case[j]
                result[j] = case[i]
                return minimize(result,i)

    #result = case[:]
    #result.insert(0,0)
    #for i in range(len(case)-1,0,-1):
    #    if case[i] > 0:
    #        result[i+1] = 0
    #        result[0] = case[i]
    #        return minimize(result,0)

def minimize(case,ind):
    rem = case[ind+1:]
    rem.sort()
    case[ind+1:] = rem    

    if case[0] == 0:
        case.pop(0)

    return case
###############################################################################
# Main                                                                        #
###############################################################################

input  = open(sys.argv[1])
output = open(sys.argv[1].replace('in','out'),'w')
#debug  = open(sys.argv[1].replace('in','debug'),'w')

nCases = int(input.readline().strip())

for i in range(nCases):
    tmp = input.readline().strip();

    case = []
    for d in tmp:
        case.append(int(d))

    #print "Case #" + str(i+1) + ": " + str(case)

    tmp2 = handleCase(case)   

    result = ""
    for d in tmp2:
        result += str(d)
    print "Case #" + str(i+1) + ": " + str(result)
    output.write('Case #' + str(i+1) + ": " + str(result) + '\r\n')


