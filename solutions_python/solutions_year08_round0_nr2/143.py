#dataset = 'small'
dataset = 'large'

fin = open('B-%s.in' % dataset, 'r')
fout = open('B-%s.out' % dataset, 'w')

def timeToMin(timeStr):
    """ timeToMin('3:41') == 3*60 + 41 """
    [hours, minutes] = [int(x) for x in timeStr.split(':')]
    return hours*60 + minutes

# testing timeToMin()
#timeList = ['3:41', '9:20', '19:05']
#print [timeToMin(x) for x in timeList]
    
def mainCalculation(triplist, readylist):
    nStart = 0
    for trip in triplist:
        try:
            trainWaiting = (readylist[0] <= trip[0])
        except IndexError:
            trainWaiting = False

        if trainWaiting: # if there will be a train waiting for me
            readylist = readylist[1:] # take it!
        else:
            nStart += 1 # we need to have one ready
    return nStart

ncases = int(fin.readline())

for i in range(ncases):
    case = i+1
    turn = int(fin.readline()) # turnaround time
    
    # number of trips A->B and B->A
    [nAB, nBA] = [int(x) for x in fin.readline().split(' ')]
    
    # if a time T is in readyAtA, it means a train will be ready to leave from A
    # at that time, having just arrived from B and finished its turnaround time 
    readyAtA = list()
    readyAtB = list()
    
    tripsAB = list()
    tripsBA = list()
    
    for j in range(nAB):
        tripsAB.append([timeToMin(t) for t in fin.readline().split(' ')])
    for j in range(nBA):
        tripsBA.append([timeToMin(t) for t in fin.readline().split(' ')])
    
    # may be necessary, but i don't think so
    tripsAB.sort()
    tripsBA.sort()
    
    for trip in tripsAB:
        readyAtB.append(trip[1]+turn)
    for trip in tripsBA:
        readyAtA.append(trip[1]+turn)
    
    # definitely necessary, unless min() is used or something
    readyAtA.sort()
    readyAtB.sort()
    
    nStartA, nStartB = mainCalculation(tripsAB, readyAtA), mainCalculation(tripsBA, readyAtB)  
    
    outputStr = "Case #%d: %d %d" % (case, nStartA, nStartB)
    
    debug = False
    if debug: # debug
        print "Case #%d:" % (case,)
        for var in ('turn', 'tripsAB', 'tripsBA', 'readyAtA', 'readyAtB', 'nStartA', 'nStartB'):
            print '%s=%s' % (var, eval(var))
    if not debug: print outputStr
         
    fout.write(outputStr+'\n')
    
fout.close()