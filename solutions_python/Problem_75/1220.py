

#inFile = "02_test.txt"
outFile = "02out_sm.txt"
inFile = "02in_sm.txt"
#inFile = "03in_lg.txt"



def getInput(filename, delim=' '):
    f = open(filename,"r")
    indata = list()
    for line in f:
        indata.append(line.strip().split(delim))
    return indata

        


def compute( inData ):
    basePairs = {}
    oppPairs = {}
    bag = []
    table = []
        
    bp = int(inData[0])
    for i in xrange(1,1+bp):
        basePairs[inData[i][0:2]] = inData[i][2]
        basePairs[(inData[i][0:2])[::-1]] = inData[i][2]
    op = int(inData[1+bp])
    for i in xrange(2+bp, 2+bp+op):
        oppPairs[inData[i][0]] = inData[i][1]
        oppPairs[inData[i][1]] = inData[i][0]        

    bag = list(inData[-1])
#    print basePairs, oppPairs, bag

    for s in bag:        
        if len(table) > 0 and table[-1]+s in basePairs.keys():
            #check for combine
            c = basePairs[table[-1]+s]
            table.pop()
            table.append(c)
        elif(s in oppPairs.keys() and oppPairs[s] in table):
            #check for opposition
            table = []
        else:
            table.append(s)
            
    return printTable(table)

def printTable(table):
    out = '['
    for i in xrange(len(table)):
        out += table[i]
        if( i < len(table)-1):
            out += ", "
    return out + "]"
    
    


# ================= MAIN ===================================

inData = getInput(inFile)

cases = int(inData[0][0])
for i in xrange(1,cases+1):
    print "Case #" + str(i) + ": " + compute(inData[i])


    
