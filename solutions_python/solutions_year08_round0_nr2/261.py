import sys


def train(filename):
    f = open(filename,'rb')
    line = f.readline()
    N = int(line.rstrip()) # N is the number of test cases
##    print 'Test Case Number: ' + str(N)
    results = []
    for i in range(N):
        result = [0,0]
        StartList = []
        StartFromA = []
        ArriveAtB  = []
        StartFromB = []
        ArriveAtA  = []
##        print 'Test Case '+str(i+1)+':'
        T = int(f.readline().rstrip()) # T is the turnaround time
##        print 'turnaround time: ' + str(T)
        Trips = [int(trip) for trip in f.readline().rstrip().split(' ')] # Trips is the number of trips from A and B, like  "2 2"
##        print 'Departure from A: ' + str(Trips[0])
##        print 'Departure from B: ' + str(Trips[1])
        for j in range(Trips[0]):
            fromA = f.readline().rstrip().split(' ')
            starttime = fromA[0].split(':')
            endtime = fromA[1].split(':')
            StartFromA.append([int(starttime[0]) * 60 + int(starttime[1]), int(endtime[0]) * 60 + int(endtime[1])])
##        print StartFromA
        for j in range(Trips[1]):
            fromB = f.readline().rstrip().split(' ')
            starttime = fromB[0].split(':')
            endtime = fromB[1].split(':')
            StartFromB.append([int(starttime[0]) * 60 + int(starttime[1]), int(endtime[0]) * 60 + int(endtime[1])])
##        print StartFromB
        StartFromA.sort()
        StartFromB.sort()
        
        #main algorithm        
        for i in range(len(StartFromA)+len(StartFromB)):
            item = None
            if (len(StartFromB) > 0 and len(StartFromA) > 0 and StartFromA[0] <= StartFromB[0]) or (len(StartFromB) == 0 and len(StartFromA) > 0):
                item = StartFromA.pop(0)
                if len(ArriveAtA) == 0:
                    result[0] += 1
                else:
                    ArriveAtA.sort()
                    if ArriveAtA[0] <= item[0]:
                        ArriveAtA.pop(0)
                    else:
                        result[0] += 1
                ArriveAtB.append(item[1]+T)
            else:
                item = StartFromB.pop(0)
                if len(ArriveAtB) == 0:
                    result[1] += 1
                else:
                    ArriveAtB.sort()
                    if ArriveAtB[0] <= item[0]:
                        ArriveAtB.pop(0)
                    else:
                        result[1] += 1
                ArriveAtA.append(item[1]+T)
        results.append(result)
        
##    print 'Results: '
    k = 1
    for result in results:
        print 'Case #'+ str(k)+': '+str(result[0])+' '+str(result[1])
        k+=1
    f.close()



if __name__ == '__main__':
    train(sys.argv[1])
