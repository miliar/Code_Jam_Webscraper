fil=open('B-large.in','r')
noc=int(fil.readline())
i=0
p = open("largerever2.in","w")
while i<int(noc):
    inputset = fil.readline().split()
    C = float(inputset[0])
    F = float(inputset[1])
    X = float(inputset[2])
    timesum = 0.0
    speed = 2.0
    time = C/speed
    while X/speed > time+ X/(F+speed):
        speed = speed + F
        timesum += time
        time = C/speed

    timesum+=X/speed
    p.write("Case #"+str(i+1)+": "+str(timesum)+"\n")
        

    

    i=i+1
p.close()
fil.close()
