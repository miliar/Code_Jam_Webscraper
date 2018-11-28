import sys

fh = open("inputs/%s" % sys.argv[1], 'r')
lines = fh.readlines()

A = 0
B = 1

def loadTime(timePair, dept, arriv):
    global events, A, B, turnTime
    times = timePair.split(' ')
    
    (hour, min) = times[0].split(':')
    time = (int(hour)) * 60 + int(min)
    if time not in events[dept]:
        events[dept][time] = -1
    else:
        events[dept][time] -= 1
        
    (hour, min) = times[1].split(':')
    time = (int(hour)) * 60 + int(min) + turnTime
    if time not in events[arriv]:
        events[arriv][time] = 1
    else:
        events[arriv][time] += 1

index = 0
cases = int(lines[index])
index += 1 
output = open("outputs/B.out", 'w')
for case in range(0, cases):
    events = [{}, {}]    
    turnTime = int(lines[index])
    index += 1    
    nTrans = [int(num.rstrip('\n')) for num in lines[index].split(' ')]
    index += 1
    #print "nTrans: %s" % nTrans
    for timePair in lines[index:index+nTrans[A]]:
        loadTime(timePair.rstrip('\n'), A, B)
    index += nTrans[A]
    for timePair in lines[index:index+nTrans[B]]:
        loadTime(timePair.rstrip('\n'), B, A)
    index += nTrans[B]
    
    #print "Events: %s" % events
    trainsReq = [0, 0]
    for i in range(0, 2):
        times = [time for time in events[i].keys()]
        times.sort()
        if not times:
            continue
        trainCount = 0
        for time in times:
            trainCount += events[i][time]
            #print "i: %s Time: %s Event: %s TrainCount: %s TrainReq: %s" % (i, time, events[i][time], trainCount, trainsReq[i])            
            if trainCount < 0:
                trainsReq[i] += (-trainCount)
                trainCount = 0
    
    output.write("Case #%i: %s %s\n" % (case+1, trainsReq[A], trainsReq[B]))