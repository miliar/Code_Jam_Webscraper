rf = open('A-large.in', 'r')
wf = open('A-large.out', 'w')
lineTotalNum = rf.readline()

for lineCounter in range(int(lineTotalNum)):
    line = rf.readline()
    lineArr = line.split(' ')
    maxSLvl = lineArr[0]
    audienceData = lineArr[1]

    accumAudience = 0
    neededFriends = 0
    for sLvl in range(int(maxSLvl)+1):
        audienceNum = int(audienceData[sLvl])
        if audienceNum > 0 and sLvl > accumAudience:
            neededAudience = sLvl - accumAudience
            neededFriends = neededFriends + neededAudience
            accumAudience = accumAudience + neededAudience
        accumAudience = accumAudience + audienceNum
        
    wf.write("Case #" + str(lineCounter+1) + ": " + str(neededFriends) + "\n")

rf.close()
wf.close()
