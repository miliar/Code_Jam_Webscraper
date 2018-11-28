def cookies(C, F, X):
    sec = 0
    rate = 2.0
    timeFarm = C / rate
    timeX = X / rate
    timeX2 = X / (rate + F) 
    while timeFarm + timeX2 < timeX:
        sec += timeFarm
        rate += F
        timeFarm = C / rate
        timeX = X / rate
        timeX2 = X / (rate + F)
    sec += timeX
    return "{0:.7f}".format(sec)
test = open("B-large.in", 'r')
outfile = open("COOKIE.DATA", 'w')
result = []
T = int(test.readline())
for j in range(1, T+1):
    data = test.readline()
    data = data.split()
    C = float(data[0])
    F = float(data[1])
    X = float(data[2])
    result.append("Case #" + str(j) + ": " + str(cookies(C, F, X)))
for i in result:
    outfile.write(i + '\n')
outfile.close()
test.close()

