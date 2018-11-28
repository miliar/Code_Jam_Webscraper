f = open('CookieCutter.txt')
lines = f.readlines()
f.close()

output = open('CookieCutterOutput.txt','w')
for i in range(int(lines[0])):
    cost_farm = float(lines[i+1].split()[0])
    farm_rate = float(lines[i+1].split()[1])
    goal = float(lines[i+1].split()[2])
    rate = 2.0
    time = 0.0    
    time_for_goal = goal/rate
    while (((cost_farm/rate) + goal/(rate+farm_rate)) < goal/rate):
        time_for_farm = cost_farm/rate
        time += time_for_farm
        rate += farm_rate
        time_for_goal = goal/rate
    time += goal/rate    
    output.write("Case #" + str(i+1) + ": " + str(time) + "\n")
output.close() 