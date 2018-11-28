fileOpen=open("B-large.in","r+")
fileOpen2=open("cca.txt","w+")
testCases=int(fileOpen.readline())
for i in range(1,testCases+1):
    testLine=((fileOpen.readline().split()))
    c=float(testLine[0])
    f=float(testLine[1])
    x=float(testLine[2])
    time=999999.0000000
    cumulativeTime=0.0
    rate=2
    normalTime=x/rate
    while(normalTime<time):
        cumulativeTime=(cumulativeTime+(c/rate))
        time=normalTime
        rate=rate+f
        normalTime=cumulativeTime+(x/rate)
    fileOpen2.write('Case #%d: %.7f\n'%(i,time))
        