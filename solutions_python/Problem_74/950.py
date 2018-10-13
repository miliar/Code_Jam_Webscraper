
with open('bots.in', 'r') as fin:
    lines = fin.readlines()
    T = int(lines[0])

for t in range(T):
    line = lines[t+1]
    bits = line.split()
    N = int(bits[0])
    orange = [] #(index, button)
    blue = []
    for n in range(N):
        if bits[n*2 + 1] == 'O':
            # add to orange list
            orange.append((n, int(bits[n*2 + 2])))
        else:
            # add to blue list
            blue.append((n, int(bits[n*2 + 2])))
    #print "Orange:", orange
    #print "Blue:", blue
    bluen = 0
    orangen = 0
    bluepos = 1
    orangepos = 1
    time = 0
    for nextbutton in range(N):
        if (bluen < len(blue) and blue[bluen][0] == nextbutton):
            timedelta = abs(bluepos - blue[bluen][1]) + 1
            time += timedelta
            bluepos = blue[bluen][1]
            bluen += 1
            if orangen < len(orange):
                if (orangepos < orange[orangen][1]):
                    orangepos = min(orangepos + timedelta, orange[orangen][1])
                else:
                    orangepos = max(orangepos - timedelta, orange[orangen][1])
        elif (orange[orangen][0] == nextbutton):
            timedelta = abs(orangepos - orange[orangen][1]) + 1
            time += timedelta
            orangepos = orange[orangen][1]
            orangen += 1
            if bluen < len(blue):
                if (bluepos < blue[bluen][1]):
                    bluepos = min(bluepos + timedelta, blue[bluen][1])
                else:
                    bluepos = max(bluepos - timedelta, blue[bluen][1])

    print "Case #{0}: {1}".format(t + 1, time)
            

    
