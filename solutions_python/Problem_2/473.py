import datetime

def createWorklist(origin, destination, turnaround):
    worklist = []
    for row in origin:
        worklist.append((datetime.datetime.strptime(row[0],'%H:%M'),'L'))
    for row in destination:
        worklist.append((datetime.datetime.strptime(row[1],'%H:%M')+datetime.timedelta(minutes=turnaround),'A'))
    worklist.sort()
    return worklist
    
def calculateRequiredNumber(worklist):
    required = 0
    available = 0
    for row in worklist:
        if row[1] == 'A':
            available = available + 1
        if row[1] == 'L':
            required = required + 1
            if available > 0:
                available = available - 1
                required = required - 1
    return required

for case in range(input()):
    T = int(raw_input());
    NA, NB = raw_input().split();
    NAList = []
    NBList = []
    for trip in range(int(NA)):
        NAList.append(raw_input().split())
    for trip in range(int(NB)):
        NBList.append(raw_input().split())
    worklist = createWorklist(NAList, NBList,T)
    startA = calculateRequiredNumber(worklist)
    worklist = createWorklist(NBList, NAList,T)
    startB = calculateRequiredNumber(worklist)
    print "Case #%d: %d %d" % (case + 1, startA, startB)