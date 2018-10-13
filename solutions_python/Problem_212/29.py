from sys import stdin as cin;

data=cin.readline
cases=int(data());

for case in range(1, cases+1):
    line=data().split()
    
    numGroups=int(line[0])
    packSize=int(line[1])
    
    line=data().split()
    groups=[int(line[n]) for n in range(numGroups)]
    
    numFresh=0
    
    if packSize==2:
        evenGroups=[]
        oddGroups =[]
        for group in groups:
            if group & 1 == 0:
                evenGroups.append(group)
            else:
                oddGroups.append(group)
        numFresh=len(evenGroups)+(len(oddGroups)+1)//2
    if packSize==3:
        threeMulGroups =[]
        threeMulPlusOne=[]
        threeMulPlusTwo=[]
        for group in groups:
            if group % 3 == 0:
                threeMulGroups.append(group)
            elif group % 3 == 1:
                threeMulPlusOne.append(group)
            else:
                threeMulPlusTwo.append(group)
        if len(threeMulPlusOne)<len(threeMulPlusTwo):
            numFresh=len(threeMulGroups)+len(threeMulPlusOne)+(len(threeMulPlusTwo)-len(threeMulPlusOne)+2)//3
        else:
            numFresh=len(threeMulGroups)+len(threeMulPlusTwo)+(len(threeMulPlusOne)-len(threeMulPlusTwo)+2)//3
            
    
    print('Case #'+str(case)+':', numFresh)