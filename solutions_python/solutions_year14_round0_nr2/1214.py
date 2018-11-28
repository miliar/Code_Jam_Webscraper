#!/usr/bin/python

inp = open('large.in', 'r')
out = open('out', 'w')

times = int(inp.readline().strip())

i = 0

while i < times:
    parts = inp.readline().strip().split(' ')
    C = float(parts[0])
    F = float(parts[1])
    X = float(parts[2])

    speed = 2.0
    totalTime = 0.0
    m = 10000000
    while True:
        waitFinish = X / speed

        if (waitFinish + totalTime) < m:
            m = waitFinish + totalTime

        if waitFinish + totalTime > m:
            break

        nextTime = C / speed 
        speed = speed + F

        totalTime = totalTime + nextTime
    
    outLine = "Case #" + str(i+1) + ": " + str(m)
    print outLine
    out.write(outLine + "\n")

    i = i + 1

inp.close()
out.close()

