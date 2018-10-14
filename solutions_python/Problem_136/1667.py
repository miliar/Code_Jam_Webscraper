def getTime(c,f,x,bought):
    time = 0
    for i in range(bought):
        time += c/(2+f*i)
    time += x/(2+f*bought)
    return time
    
f = open("B-small-attempt1.in","r")
f.readline()
t = 1
for line in f:
    line = [float(a) for a in line.split()]
    time1 = getTime(line[0],line[1],line[2],0)
    time2 = getTime(line[0],line[1],line[2],1)
    bought = 1;
    while time1 > time2:
        bought += 1
        time1 = time2
        time2 = getTime(line[0],line[1],line[2],bought)
    print("Case #"+str(t)+": "+str(round(time1,7)))
    t+=1
    
           
