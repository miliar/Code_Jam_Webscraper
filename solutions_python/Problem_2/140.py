import sys;

def timeStringToMinutes(timeString):
    temp = timeString.split(':');
    return int(temp[0])*60 + int(temp[1]);

def isTrainAvailable(trainList, deptTime):
    index = 0;
    while index < len(trainList):
        if trainList[index] <= deptTime:
            return index;
        index += 1;
    return -1;
            

baseFilename = sys.argv[1];

fIn = file(baseFilename + '.in');
fOut = file(baseFilename + '.out', 'w');

num_tests = int(fIn.readline().strip());

current_test = 0;
while current_test < num_tests:
    turnaround_time = int(fIn.readline().strip());
    (ABTrips, BATrips) = fIn.readline().strip().split(' ');
    ABTrips = int(ABTrips); BATrips = int(BATrips);    
    trips = [];
    current_read = 0;
    while current_read < ABTrips:
        (dep, arr) = fIn.readline().strip().split(' ');
        trips.append([timeStringToMinutes(dep), timeStringToMinutes(arr), 'A']);
        current_read += 1;

    current_read = 0;
    while current_read < BATrips:
        (dep, arr) = fIn.readline().strip().split(' ');
        trips.append([timeStringToMinutes(dep), timeStringToMinutes(arr), 'B']);
        current_read += 1;

    trips.sort(lambda x, y: x[0] - y[0]);

    ATrains_Created = 0;
    BTrains_Created = 0;
    TrainsAtA = [];
    TrainsAtB = [];

    for trip in trips:
        if trip[2] == 'A':
            tmp = isTrainAvailable(TrainsAtA, trip[0])
            if tmp != -1:
                TrainsAtA.pop(tmp);
            else:
                ATrains_Created += 1;
            TrainsAtB.append(trip[1] + turnaround_time);
            TrainsAtB.sort();
        else:
            tmp = isTrainAvailable(TrainsAtB, trip[0])
            if tmp != -1:
                TrainsAtB.pop(tmp);
            else:
                BTrains_Created += 1;
            TrainsAtA.append(trip[1] + turnaround_time);
            TrainsAtA.sort();

    fOut.write("Case #" + str(current_test + 1) + ": " + str(ATrains_Created) + ' ' + str(BTrains_Created) + '\n');
    current_test += 1;

fOut.close();
fIn.close();
