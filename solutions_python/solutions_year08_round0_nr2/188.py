import sys
import string

inputfile=open(r'.\B-large.in', 'r')
numofcases=string.atoi(inputfile.readline())
for i in range(numofcases):
    tt=string.atoi(inputfile.readline())
    nums=inputfile.readline().split()
    astart=string.atoi(nums[0])
    bstart=string.atoi(nums[1])
    timetable=[]
    for j in range(astart):
        time=inputfile.readline().split()
        dt=string.atoi(time[0].split(':')[0])*60+string.atoi(time[0].split(':')[1])
        at=string.atoi(time[1].split(':')[0])*60+string.atoi(time[1].split(':')[1])
        timetable.append([dt,at,'a'])
    for j in range(bstart):
        time=inputfile.readline().split()
        dt=string.atoi(time[0].split(':')[0])*60+string.atoi(time[0].split(':')[1])
        at=string.atoi(time[1].split(':')[0])*60+string.atoi(time[1].split(':')[1])
        timetable.append([dt,at,'b'])
    timetable.sort(lambda x, y: cmp(x[0],y[0]))
    #print timetable
    arrivala=[]
    arrivalb=[]
    totala=0
    totalb=0
    for each in timetable:
        if each[2]=='a':
            if len(arrivala)>0 and arrivala[0][1]+tt<=each[0]:
                arrivala.pop(0)
            else:
                totala+=1
            arrivalb.append(each)
            arrivalb.sort(lambda x, y: cmp(x[1],y[1]))
        else:
            if len(arrivalb)>0 and arrivalb[0][1]+tt<=each[0]:
                arrivalb.pop(0)
            else:
                totalb+=1
            arrivala.append(each)
            arrivala.sort(lambda x, y: cmp(x[1],y[1]))
    print 'Case #%d: %d %d' % (i+1, totala, totalb)
        
