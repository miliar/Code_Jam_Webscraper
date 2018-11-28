from decimal import *
getcontext.prec=(10)

class horse:
    def __init__(self,startPos,speed):
        self.startPos=startPos
        self.speed=speed


def GetMaxSpeed(D,horses):
    maxSpeed=None
    #For each horse, reduce our max speed so we won't get a violation
    for h in horses:
        #We want to finish at exactly the same time as them
        horseTravel=D-h.startPos
        horseTime=Decimal(horseTravel)/Decimal(h.speed) #We want floats here - we need an ans to 10e-6 precision
        desiredSpeed=Decimal(D)/horseTime
        if(maxSpeed==None): maxSpeed=desiredSpeed
        elif(desiredSpeed < maxSpeed):
            maxSpeed=desiredSpeed
            
    return maxSpeed

numCases=int(raw_input())
for case in range(numCases):
    line1=list(raw_input().split(" "))
    distance=int(line1[0])
    numHorses=int(line1[1])
    horses=[]
    for h in range(numHorses):
        horseLine=raw_input().split(" ")
        thisHorse=horse(int(horseLine[0]),int(horseLine[1]))
        horses.append(thisHorse)

    maxSpeed=GetMaxSpeed(distance,horses)
    print("Case #"+str(case+1)+": "+str(maxSpeed))

