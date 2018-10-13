import sys

###############################################################################
# Helper functions                                                            #
###############################################################################
def printArray(arr):
    for row in arr:
        for val in row:
            print str(val).rjust(3) + ' ',
        print ''

def countOccurences(line,key):
    tmp = []
    for k in range(len(key)):
        keyChar = key[k]
        tmp.append([0 for x in line])
        carry = 0
        for l in range(len(line)):
            lineChar = line[l]
            if k == 0:
                tmp[k][l] = 1 if lineChar == keyChar else 0
            else:
                carry += tmp[k-1][l]
                tmp[k][l] = carry if lineChar == keyChar else 0

#    printArray(tmp)
    count = 0
    k = len(key)-1
    for l in range(len(line)):
        count += tmp[k][l]
    return count


###############################################################################
# Main                                                                        #
###############################################################################
key = "welcome to code jam"

input  = open(sys.argv[1])
output = open(sys.argv[1].replace('in','out'),'w')
#debug  = open(sys.argv[1].replace('in','debug'),'w')

nCases = int(input.readline().strip())

for i in range(nCases):
    line  = input.readline().strip()
    count = str(countOccurences(line,key))
    print "Case #" + str(i+1) + ": " + str(count[-4:]).zfill(4)
    output.write('Case #' + str(i+1) + ": " + str(count[-4:]).zfill(4) + '\r\n')


