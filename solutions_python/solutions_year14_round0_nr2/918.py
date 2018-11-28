input = open('B-large.in','r')
text = input.read()
stringlist = text.split('\n')
numofcases = int(stringlist[0])
stringlist = stringlist[1:]

result = []
for i in range(numofcases):
    row = stringlist[0].split(' ')
    row = [float(x) for x in row]
    cost = row[0]
    farm = row[1]
    win  = row[2]
    rate = 2.0
    minitime = win / rate
    buildtime = win / (rate + farm)
    tmptime = cost / rate + buildtime
    while(tmptime < minitime):
        minitime = tmptime
        rate = rate + farm
        tmptime = tmptime - buildtime + cost / rate + win / (rate + farm)
        buildtime = win / (rate + farm)
    minitime = '%.7f' % minitime
    result.append(str(minitime))
    stringlist = stringlist[1:]

output = open('Largeoutput','w')
for i in xrange(1,len(result)+1):
    output.write('Case #%d: %s\n' % (i,result[i-1]))
output.close()

    
