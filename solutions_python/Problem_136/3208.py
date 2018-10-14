inputFile=file('B-large.in','r')

firstLine=inputFile.readline()
n=int(firstLine)
output=''
line=inputFile.readline()

for i in range(n):
    #print('i: '+str(i))
    L=[float(num) for num in line.split(' ')]
    #print(L)
    C=L[0];F=L[1];X=L[2];
    #print("C: "+str(C))
    #print("F: "+str(F))
    #print("X: "+str(X))
    farms=0.0
    totalTime=0.0

    condition=True
    while condition:
        currentRate=2+farms*F
        nextRate=2+(farms+1)*F
        #print("currentRate: "+str(currentRate))
        #print("nextRate: "+str(nextRate))

        currentFarmTime=C/currentRate
        #nextFarmTime=C/nextRate
        #print("currentFarmTime: "+str(currentFarmTime))
        #print("nextFarmTime: "+str(nextFarmTime))

        currentETA=X/currentRate
        nextETA=X/nextRate
        #print("currentETA: "+str(currentETA))
        #print("nextETA: "+str(nextETA))

        condition=currentETA>currentFarmTime+nextETA

        if condition:
            farms+=1
            totalTime+=currentFarmTime
        else:
            totalTime+=currentETA
        #print("totalTime: "+str(totalTime))
    output+="Case #"+str(i+1)+": "+str(totalTime)+"\n"
    line=inputFile.readline()

outputFile=open('output_problem_b.txt','w')
outputFile.write(output)
outputFile.close()
inputFile.close()
