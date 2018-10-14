import operator

data = open('B-large.in')
num_data = int(data.next())
for x in xrange(num_data):
    """Get data"""
    tripsFromA = []
    tripsFromB = []
    turnaround_time = int(data.next())
    num_tripsFromA, num_tripsFromB = map(int,data.next().split())
    for i in xrange(num_tripsFromA):
        trip_str = data.next().split()
        tripsFromA.append(map(lambda y: int(y.split(':')[0])*60+int(y.split(':')[1]),trip_str))
    for i in xrange(num_tripsFromB):
        trip_str = data.next().split()
        tripsFromB.append(map(lambda y: int(y.split(':')[0])*60+int(y.split(':')[1]),trip_str))
    
    """Transform data"""
    tripsFromA_sortedByStart = tripsFromA[:]
    tripsFromA_sortedByArrive = tripsFromA[:]
    tripsFromA_sortedByStart.sort()
    tripsFromA_sortedByArrive.sort(key=operator.itemgetter(1))
    
    tripsFromB_sortedByStart = tripsFromB[:]
    tripsFromB_sortedByArrive = tripsFromB[:]
    tripsFromB_sortedByStart.sort()
    tripsFromB_sortedByArrive.sort(key=operator.itemgetter(1))
    
    """Do calculation"""
    num_trainsFromA = num_tripsFromA
    num_trainsFromB = num_tripsFromB
    for tripFromA in tripsFromA_sortedByArrive:
        reused = False
        for jB in xrange(num_tripsFromB):
            if tripsFromB_sortedByStart[jB] == []:
                continue
            elif tripFromA[1] + turnaround_time <= tripsFromB_sortedByStart[jB][0]:
                num_trainsFromB -= 1
                tripsFromB_sortedByStart[jB] = []
                reused = True
                break
            # If this trip from B cannot reuse the current train won't be able to use latter arrived trains as well
            else:
                tripsFromB_sortedByStart[jB] = []
        # If no trips from B can reuse the current train, they cannot use latter arrived trains as well
        if not reused:
            break
    
    for tripFromB in tripsFromB_sortedByArrive:
        reused = False
        for jA in xrange(num_tripsFromA):
            if tripsFromA_sortedByStart[jA] == []:
                continue
            elif tripFromB[1] + turnaround_time <= tripsFromA_sortedByStart[jA][0]:
                num_trainsFromA -= 1
                tripsFromA_sortedByStart[jA] = []
                reused = True
                break
            # If this trip from A cannot reuse the current train won't be able to use latter arrived trains as well
            else:
                tripsFromA_sortedByStart[jA] = []
        # If no trips from A can reuse the current train, they won't be able to use latter arrived trains as well
        if not reused:
            break
    
    """Print results"""
    ans = [num_trainsFromA, num_trainsFromB]
    ans = map(str,ans)
    print 'Case #%s: %s' % (x+1, ' '.join(ans))    