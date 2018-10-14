__author__ = 'mehmetinan'


from __future__ import division

lines = open("B-small-attempt1.in").read().splitlines()
number = int(lines[0])

counter = 1
results = []

def totalspeed(totalcookie,pace,speed,amounttoupgrade):
    totaltime = 0.0000000
    if speed == 2.0000000:
        time = float(totalcookie/speed)
        totaltime = totaltime + time
    else:
        time = totalcookie/speed
        totaltime = float(totaltime + time)

        while True:
            speed = speed - pace
            if speed < 2.0000000:
                break
            time = float(amounttoupgrade/speed)
            totaltime = totaltime + time

    return totaltime



counter = 1
for i in range(0,number):
    defaultspeed = 2.00000001
    data = lines[counter].split()
    minimumtime = totalspeed(float(data[2]),float(data[1]),defaultspeed,float(data[0]))

    while True:
        time = totalspeed(float(data[2]),float(data[1]),defaultspeed,float(data[0]))
        if time < minimumtime:
            minimumtime = time

        if time > minimumtime:
            results.append(round(minimumtime,7))
            break

        else:
            defaultspeed = defaultspeed + float(data[1])


    counter = counter + 1



for i in range(0,len(results)):
    print 'Case #%d:  %s' % (i+1,results[i])