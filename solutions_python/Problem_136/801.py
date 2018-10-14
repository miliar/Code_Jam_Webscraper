fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N = fin.readline()

n = int(N)

for i in range(0,n):
    param = (fin.readline()).split()
    C = float(param[0])
    F = float(param[1])
    X = float(param[2])

    rate = 2
    cookies = 0
    totalTime = 0
    timeToX = X/rate
    timeToFarm = C/rate
    newTimeToX = X/(rate+F)

    while((totalTime + timeToFarm + newTimeToX) < (totalTime + timeToX)):
        rate += F
        totalTime += timeToFarm
        timeToX = newTimeToX
        timeToFarm = C/rate
        newTimeToX = X/(rate+F)

    totalTime += timeToX

    s = 'Case #'
    s+= str(i+1)
    s+= ': '
    tempStr = "%.7f" % (totalTime)
    s+= tempStr
    s+= '\n'
    fout.write(s)

fin.close()
fout.close()
