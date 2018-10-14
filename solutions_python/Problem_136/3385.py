myInbox=open("input.txt","r")
myAnswer=open("output3.txt","w")
testCase=int(myInbox.readline().strip("\n"))
parameter=[]
costToBuild=0.0000000
extraSpeed=0.00000000
goal=0.0000000
currentSpeed=2.0000000
currentTime=0.0000000
iteration=0
memo=[]
for poop in range (testCase):
    iteration=1
    print poop
    currentSpeed=2.0000000
    parameter=myInbox.readline().strip("\n").split(" ")
    parameter=[float(i) for i in parameter]
    costToBuild=parameter[0]
    extraSpeed=parameter[1]
    goal=parameter[2]
    while True:
        if (goal/currentSpeed)>((costToBuild/currentSpeed)+(goal/(currentSpeed+extraSpeed))):
           currentSpeed+=extraSpeed
           iteration+=1
        else:
            iteration+=1
            break
    for x in range(iteration):
        currentTime=0.000
        currentSpeed=2.000
        for y in range (x):
            currentTime+=(costToBuild)/currentSpeed
            currentSpeed+=extraSpeed
        currentTime+=goal/currentSpeed
        memo.append(currentTime)
        currentTime=0.000
        currentSpeed=2.000
    answer=min(memo)
    memo=[]
    myAnswer.write("Case #"+str(poop+1)+": "+str(answer)+"\n")
myAnswer.close()
myInbox.close()
