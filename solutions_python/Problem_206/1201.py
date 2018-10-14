fileName = "A-large.in"
f = open(fileName, 'r')

outputName = "A-large-out.txt"
output = open(outputName, 'w')

line = f.readline()
T = int(line)

for t in range(T):
    res = ""
    line = f.readline()
    line = line.split()
    D = int(line[0])
    D = D * 1.0
    N = int(line[1])
    horses = []

    for i in range(N):
        line = f.readline()
        line = line.split()
        K = int(line[0])
        S = int(line[1])
        horses.append([K, S])
        
    horses.sort(key=lambda x: x[0], reverse = True)
    
    for i in range(1, N):
        speed = horses[i-1][1] * 1.0
        position = horses[i-1][0] * 1.0
        time = (D - position)/speed
        
        speed2 = horses[i][1] * 1.0
        position2 = horses[i][0] * 1.0
        time2 = (D - position2)/speed2
        
        if time2 < time:
            newSpeed = (D - position2) / time
            horses[i][1] = newSpeed
    
    speed = horses[N-1][1] * 1.0
    position = horses[N-1][0] * 1.0
    time = (D - position)/speed
    
    finalSpeed = D / time
    res = "{0:.8f}".format(finalSpeed)
        
    print("Case #{}: {}".format(t+1, res))
    output.write("Case #{}: {}".format(t+1, res))
    output.write("\n")
    
output.close()