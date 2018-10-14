loops = input().strip()
loops = int(loops)
i = 1
while(i <= loops):
    line=input().strip().split()
    C=float(line[0])
    F=float(line[1])
    X=float(line[2])
    R=2
    lastTime=X/R
    buildCost = C/(R)
    total=buildCost
    R+=F
    lastTotal=0
    time=X/R
    while (True):
        time=X/R
        buildCost = C/(R)
        #print("TO="+str(total)+" TI="+str(time) + " LTO="+str(lastTotal)+" LTI="+str(lastTime))
        #print(str(total+time)  + ">" + str(lastTotal+lastTime))
        if((total+time)>(lastTotal+lastTime)):
            break
        else:
            lastTotal=total
            lastTime=time
            total+=buildCost
            R+=F
    answer = lastTotal+lastTime
    print("Case #" + str(i) +": " + str(answer))
    i+=1



