
import time

input = open("B-large.in", "r")
output = open("B-large.out", "w")

i = int(input.readline().strip())

for case in range(i):
    turnaroundTime = int(input.readline().strip())
    (AtoBNumber, BtoANumber) = map(int, input.readline().strip().split(" "))
    
    timeList = []
    for j in range(AtoBNumber):
        (departureString, arrivalString) = input.readline().strip().split(" ")
        departure = time.strptime(departureString + " 1971", "%H:%M %Y")
        #print str(departure)
        departure = time.localtime(time.mktime(departure))
        arrival = time.strptime(arrivalString + " 1971", "%H:%M %Y")
        arrival = time.localtime(time.mktime(arrival) + 60*turnaroundTime)
        timeList.append((departure, "A", "departure"))
        timeList.append((arrival, "B", "arrival"))
    for j in range(BtoANumber):
        (departureString, arrivalString) = input.readline().strip().split(" ")
        departure = time.strptime(departureString + " 1971", "%H:%M %Y")
        departure = time.localtime(time.mktime(departure))
        arrival = time.strptime(arrivalString + " 1971", "%H:%M %Y")
        arrival = time.localtime(time.mktime(arrival) + 60*turnaroundTime)
        timeList.append((departure, "B", "departure"))
        timeList.append((arrival, "A", "arrival"))
        
    timeList.sort();
        
    tmpAtoB = 0
    tmpBtoA = 0
    
    AtoB = 0
    BtoA = 0
    
    for timeTable in timeList:
        if timeTable[2] == "arrival":
            if timeTable[1] == "A":
                tmpAtoB += 1
            else:
                tmpBtoA += 1
        else:
            if timeTable[1] == "A":
                if tmpAtoB > 0:
                    tmpAtoB -= 1
                else:
                    AtoB +=1
            else:
                if tmpBtoA > 0:
                    tmpBtoA -=1
                else:
                    BtoA += 1
                    
    output.write("Case #%d: %d %d\n" %(case+1, AtoB, BtoA))
                      