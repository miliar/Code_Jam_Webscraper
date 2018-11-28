#!/usr/bin/python
f=open('input', 'r+')
case=f.readline()
for i in range(int(case)):
    firstLine=int(f.readline())-1
    firstMatrix=eval('[['+f.readline().replace(' ',',').rstrip('\n')+'],['+f.readline().replace(' ',',').rstrip('\n')+'],['+f.readline().replace(' ',',').rstrip('\n')+'],['+f.readline().replace(' ',',').rstrip('\n')+']]')
    secondLine=int(f.readline())-1
    secondMatrix=eval('[['+f.readline().replace(' ',',').rstrip('\n')+'],['+f.readline().replace(' ',',').rstrip('\n')+'],['+f.readline().replace(' ',',').rstrip('\n')+'],['+f.readline().replace(' ',',').rstrip('\n')+']]')
    inter=list(set(firstMatrix[firstLine]).intersection(secondMatrix[secondLine]))
    if len(inter)==1:
        print "Case #"+str(i+1)+": "+str(inter[0])
    elif len(inter)>1:
        print "Case #"+str(i+1)+": Bad magician!"
    else:
        print "Case #"+str(i+1)+": Volunteer cheated!"


