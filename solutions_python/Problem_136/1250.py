import math
filein = open("PBsmall.txt", "r")
out = open("PBsmallout.txt", "w")

cases = int(filein.readline())
for i in xrange(cases):
    line = filein.readline()
    C = float(line.split()[0])
    F = float(line.split()[1])
    X = float(line.split()[2])
    rate = 2
    time = 0
    cur = 0
    while cur < X:
        if(X-cur)/rate < ((C-cur)/rate + (X - cur)/(rate+F)):
            time += (X-cur)/rate
            cur = X
        else:
            time += (C-cur)/rate
            rate += F
            cur = 0
    out.write("Case #" + str(i+1) + ": " + str(round(time,7))+"\n")
out.close()
filein.close()
