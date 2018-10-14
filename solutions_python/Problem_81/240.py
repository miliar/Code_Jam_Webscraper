import sys
import math

lines = sys.stdin.readlines()
count = 1
cases = int(lines[0])
place = 1

for count in range(cases):
    N = int(lines[place])

    w = dict()
    l = dict()
    
    team = 0

    for row in lines[place+1:place+1+N]:
        w[team] = float(0)
        l[team] = float(0)
        for res in row:
            if res == '1':
                w[team] += 1
            elif res == '0':
                l[team] += 1

        team +=1

    wp = dict()
    for i in range(N):
        wp[i] = w[i] / (w[i] + l[i])
        #print wp[i]

    owp = dict()
    team = 0
    for row in lines[place+1:place+1+N]:
        owp[team] = float(0)
        matches = float(0)
        for index,res in enumerate(row):
            if res == '1':
                owp[team] += w[index] / (w[index] + l[index] - 1)
                matches += 1
            elif res == '0':
                owp[team] += (w[index]-1) / (w[index] + l[index] - 1)
                matches += 1

        if(matches > 0):
            owp[team] = owp[team]/matches

        team +=1    

    #print owp

    oowp = dict()
    team = 0
    for row in lines[place+1:place+1+N]:
        oowp[team] = float(0)
        matches = float(0)
        for index,res in enumerate(row):
            if res == '1' or res == '0':
                oowp[team] += owp[index]
                matches += 1
        if (matches > 0):
            oowp[team] = oowp[team] / matches

        team += 1

    print "Case #" + str(count + 1) + ":"
    
    #print wp, owp, oowp
    for team in range(N):
        #print wp[team]
        #print owp[team]
        #print oowp[team]
        print (.25*wp[team] + .5*owp[team] + .25*oowp[team])
        #print "----"

    place = place + N + 1
