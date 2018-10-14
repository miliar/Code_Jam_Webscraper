from sys import stdin

T = int(stdin.readline())

for trial in xrange(1,T+1):
    sMax, digits = map(str, stdin.readline().split())
    totPeople = 0
    peopleNeeded = 0
    for shynessLevel,numPeople in enumerate(map(int,digits)):
        if totPeople<shynessLevel and numPeople>0:
            x = shynessLevel-totPeople
            peopleNeeded+=x
            totPeople+=x
        totPeople+=numPeople
    print "Case #%s: %s" % (trial,peopleNeeded)
        