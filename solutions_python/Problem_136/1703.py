file = open("in.txt")

lineNumber = 0
for line in file:
    if lineNumber == 0:
        lineNumber = 1
        continue
    line = line.strip().split()
    
    cost = float(line[0])
    farm_production = float(line[1])
    winning_threshold = float(line[2])

    farms_to_buy = 0
    times = []
    while True:
        production = 2
        time = 0

        for i in range(farms_to_buy):
            time += cost/production
            production += farm_production

        
        time += winning_threshold/production

        if len(times)>0 and time > times[-1]:
            break

        times.append(time)

        
        farms_to_buy += 1

    sol = times[-1]
    print("Case #{}: {:.7f}".format(lineNumber,sol))
    lineNumber += 1
