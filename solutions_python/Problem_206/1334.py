def horses(horses, length):
    # lastHorse=horse[0]
    lastTime = float(length - horses[0][0]) / horses[0][1]
    time = 0
    for horse in horses:
        time = float(length - horse[0]) / horse[1]
        if (lastTime < time):
            lastTime = time
    speed = length / lastTime
    return speed

f=open("C:\\Users\\Saar\\Desktop\\input.txt",'r')
f2=open("C:\\Users\\Saar\\Desktop\\output.txt",'w')
lines=f.readlines()[1:]
r=""
t=""
myHorses=[]
counter=0
length=0
caseCounter=1
for line in lines:
	r,t=line.split(' ')
	if (counter==0):
		myHorses=[]
		counter=int(t)
		length=int(r)
		continue
	myHorses.append((int(r),int(t)))
	if (counter==1):
		f2.write("Case #"+str(caseCounter)+": "+str(horses(myHorses,length))+"\n")
		caseCounter+=1
	counter-=1
f.close()
f2.close()