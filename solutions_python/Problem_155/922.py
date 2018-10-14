def doCase(line):
    extras = 0
    totalStanding = 0
    case = line[1]
    
    for shyness in range(0, int(line[0]) + 1):
        if (int(case[shyness]) > 0):
            if (extras + totalStanding < shyness):
                extras += shyness - (totalStanding + extras)
        
            totalStanding += int(case[shyness])
        
    return extras



lines = [line.strip().split() for line in open('A-large.in')]

out = open('output.txt', 'w')
for i in range(1, int(lines[0][0]) + 1):
    out.write("Case #" + str(i) + ": " + str(doCase(lines[i])) + "\n")
out.close