#test.txt
input = open('B-large.in','r')
output = open('outputLarge.txt','w')
line = input.readline()
line = line.replace("\n","")
numberOfTestCases = int(line.split(" ")[0])
for i in range(numberOfTestCases):
    line = input.readline()
    line = line.replace("\n","")
    array = line.split(" ")
    numberOfGooglers = int(array[0])
    surpiseTriplet = int(array[1])
    totalPoints = int(array[2])
    winners = 0
    failedAve = []
    for googler in range(numberOfGooglers):
        points = int(array[googler+3])
        average = int(points/3)
        remainder = points % 3
        if remainder == 0:
            if average >= totalPoints:
                winners+=1;
            else:
                if average !=0:
                    failedAve.append(average)
                    failedAve.append(remainder)
        elif remainder == 1 or remainder == 2:
            if average+1 >= totalPoints:
                winners+=1;
            else:
                failedAve.append(average)
                failedAve.append(remainder)
    failedValue = 0
    while failedValue <len(failedAve):
        average = failedAve[failedValue]
        failedValue+=1
        remainder = failedAve[failedValue]
        failedValue+=1
        if surpiseTriplet >0:
            if remainder == 0 or remainder == 1:
                if average+1 >= totalPoints:
                    winners+=1
                    surpiseTriplet-=1
            elif remainder == 2:
                if average+2 >= totalPoints and average+2 <=10:
                    winners+=1
                    surpiseTriplet-=1
    output.write("Case #"+str(i+1)+": "+str(winners)+"\n")

        