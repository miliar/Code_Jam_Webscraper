import sys

inputFile = sys.argv[1]

with open(inputFile, "r") as file:
    T = int(file.readline())
    for test in range(1, T + 1):
        c, f, x = map(float, file.readline().split())
        
        rate = 2.0
        bestTime = x / rate;
        currentTime = 0.0
        
        while True:
            timeToNextFarm = c / rate
            currentTime += timeToNextFarm
            rate += f
            forecast = currentTime + (x / rate)
            if (forecast < bestTime):
                bestTime = forecast
            else:
                break
        
        output = bestTime
        print "Case #{0}: {1}".format(test, output)