import numpy as np
import sys
COUNTCASE = 1
if (len(sys.argv)==1):
    print('Required argument : sample file\n')
    exit()
result = open('result','w')
sample = open(sys.argv[1],'r')

nblines = sample.readline()
for k in range (int(nblines)):
    firstline = sample.readline()
    data = firstline.split()
    distance = int(data[0])
    nbhorses = int(data[1])
    
    timemax = 0
    for i in range (nbhorses):
        horseline = sample.readline()
        horsedata = horseline.split()
        N = int(horsedata[0])
        S = int(horsedata[1])

        value = 1.0*(distance - N)/(1.0*S)
        if (value > timemax):
            timemax = value
    res = (1.0*distance) / (1.0*timemax)

    result.write('Case #' + str(COUNTCASE) + ': ' + str(res) + '\n')
    COUNTCASE += 1

result.close()
sample.close()
