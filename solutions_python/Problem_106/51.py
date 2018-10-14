#Cars!
from math import *

def disp(a, vo, t):
    return vo*t + 0.5*a*t*t


t = int(raw_input())
for case in range(0,t):
    input = raw_input().split(" ")
    distance = float(input[0])
    N = int(input[1])
    a = int(input[2])

    time = []
    dis = []
    
    for n in range(1,N+1):
        row = raw_input().split(" ")
        time.append(float(row[0]))
        dis.append(float(row[1]))

    accel = raw_input().split(" ")

    finals = []
    for acc in accel:
        acc = float(acc)
        ydis = 0
        yvel = 0

        i = 0
        ydistemp = 0
        finalT = 0

        for i in range(0,N):
            xi = dis[i]
            ti = time[i]
#            i += 1
            if i != 0:
                ydis += disp(acc,yvel,ti-time[i-1])

            if ydis > distance:
                ddelta = distance-ydistemp
                extraT = (-yvel + sqrt(yvel*yvel + 2 * ddelta * acc)) / acc
                otherT = (distance - dis[i-1])/((dis[i]-dis[i-1])/(time[i]-time[i-1]))

                finalT = max(extraT, otherT)
#                print extraT, otherT
#                break

            if ydis > xi:
                ydis = xi
                yvel = (xi-dis[i-1])/(ti-time[i-1])
            
            else:
                if i != 0:
                    yvel += (ti-time[i-1])*acc
            
#            print xi,ti,ydis,yvel,acc


            ydistemp = ydis
        if ydis < distance:
#            print ydis
            ddelta = distance-ydistemp
#            print ddelta
            extraT = (-yvel + sqrt(yvel*yvel + 2 * ddelta * acc)) / acc
            finalT = extraT + ti
        
        finals.append(finalT)

    print "Case #" + str(case+1) + ": "
    for finalTime in finals:
        print finalTime
