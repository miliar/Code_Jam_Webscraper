input = open('B-large.in','r');
output = open('output.txt','w');

nrTestCases = int(input.readline());

line = input.readline().strip('\n');
case = 1;
while line != '':
    print "Case #%d" % case
    values = line.split(' ');
    nrSpeedBosters = int(values[0])
    speedBoosterTime = int(values[1])
    nrStars = int(values[2])
    nrDistances = int(values[3])
    distances = []
    for i in range(0,nrDistances):
        distances.append(int(values[4 + i]))
    
    allDistances = [];
    k = 0;
    totalDist = 0;
    while 1:
        for i in range(0,nrDistances):
            start, end = k * nrDistances + i,k * nrDistances + i + 1
#            print "distance: %d" % distances[i]
            begin = totalDist;
            totalDist += distances[i]
            possSpeedUp = 0;
            if 2 * totalDist - speedBoosterTime > 0:
                elapsedTime = 2 * begin;
                subtractor = max(0, speedBoosterTime - elapsedTime)
                possSpeedUp = distances[i] - subtractor * 0.5
            
#            print "possible speed up distance: %d " % (possSpeedUp)
#            print start, end, distances[i]
            allDistances.append([distances[i], possSpeedUp]);
            if end == nrStars:
                break;
        
        if end == nrStars:
            break;

        k += 1;
    
    allDistances = sorted(allDistances, key=lambda distance: distance[1], reverse=True) 
    #print allDistances;

    totalDuration = 0;
    usedBoosts = 0;
    for distance in allDistances:
        if usedBoosts < nrSpeedBosters:
            durationWithout = (distance[0] - distance[1]) * 2
            totalDuration += distance[1] + durationWithout;
            usedBoosts += 1;
        else:
            totalDuration += 2 * distance[0];
    
    output.write('Case #%d: %d\n' % (case, totalDuration));

    case += 1;
    line = input.readline().strip('\n');
