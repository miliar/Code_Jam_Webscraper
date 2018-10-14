import sys
N = int(sys.stdin.readline())

def dateStringToInt(st):
    sts = st.split(':')
    return 60*int(sts[0]) + int(sts[1])

def getPlan(length):
    plan = []
    for _ in range(length):
        tripLineSplit = sys.stdin.readline().split(' ')
        plan.append( ( dateStringToInt(tripLineSplit[0]), dateStringToInt(tripLineSplit[1].rstrip('\n')) ) )
    return plan

def buildEvents(planA, planB, T):
    scheduleA = []
    scheduleB = []
    for (dep, arr) in planA:
        #plan A - departments are +1needed in scheduleA
        #arrivals are -1needed in scheduleB (at time arr+T)
        scheduleA.append( (dep,  1, 'a') )
        scheduleB.append( (arr+T, -1, 'b') )
    for (dep, arr) in planB:
        #plan B - departments are +1needed in scheduleB
        #arrivals are -1needed in scheduleA (at time arr+T)
        scheduleB.append( (dep,  1, 'b') )
        scheduleA.append( (arr+T, -1, 'a') )
    return (scheduleA, scheduleB)


for caseNumber in range(1,N+1):
    T = int(sys.stdin.readline())
    line = sys.stdin.readline().split(' ')
    NA = int(line[0])
    NB = int(line[1])
    planA = getPlan(NA)
    planB = getPlan(NB)
    
    (scheduleA, scheduleB) = buildEvents(planA, planB, T)
    schedule = scheduleA+scheduleB
    schedule.sort()
    
    neededA = 0
    neededB = 0
    waitingA = 0
    waitingB = 0
    for (_time, status, station) in schedule:
        if station == 'a':
            if status == 1: #departs from station a
                if waitingA == 0: #there is none waiting
                    neededA += 1 #spawn another one, so it can depart
                else: #if there are any waiting
                    waitingA -= 1 #let him go
            else: #arrives to station a    status == -1
                waitingA += 1
        else: #station == 'b'
            if status == 1: #departs from station b
                if waitingB == 0: #there is none waiting
                    neededB += 1 #spawn another one, so it can depart
                else: #if there are any waiting
                    waitingB -= 1 #let him go
            else: #arrives to station b
                waitingB += 1
    
    sys.stdout.write('Case #%s: %s %s\n' % (caseNumber, neededA, neededB))
