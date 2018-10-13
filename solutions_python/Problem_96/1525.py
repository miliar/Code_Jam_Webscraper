#Problem B
#Dancing with the Googlers

from itertools import combinations


filename = open("B-small-attempt13.in",'r')
s = filename.readlines()
for i in range(len(s)):
    s[i] = s[i].replace("\n","")
filename.close()

testCases=s[0]
n = range(11)*3
x=combinations(n,3)
y=[]
for i in x:
    y.append(i)
x=[]
for i in set(y):
    if max(i) - min(i) <= 2:
        x.append(i)

surprisingNumbers =[]
notSurprising = []
for i in range(31):
    surprisingNumbers.append([i,[]])
    notSurprising.append([i,[]])
    
for i in x:
    total = sum(i)
    if max(i)-min(i)==2:
        surprisingNumbers[total][1].append(i)
    else:
        notSurprising[total][1].append(i)

for i in notSurprising:
	check = i[1][-1]
	for j in i[1][1:]:
		if sorted(j)==sorted(check):
			check = j
	if check == i[1][-1]:
		i[1]=check

for i in surprisingNumbers:
    try:
        check = i[1][-1]
        for j in i[1][1:]:
            if sorted(j)==sorted(check):
                check = j
        if check == i[1][-1]:
            i[1]=check
    except:
        continue

def outputList(googlers,surprising,q,e,b,z):
    """q is the surprising numbers, e is both"""
    #print q,e,surprising,googlers,b,z
    """
    if b==googlers:
        return b
    if q==0 and e==0:
        return 0
    if q>= surprising and e==0:
        return surprising
    if q==0 and e==0 and surprising >0:
        return 0
    """
    if googlers ==1:
        if surprising ==1:
            
            if q==1 and e==0 and b==0 and z==0:
                return 1
            if q==0 and e==1 and b==0 and z==0:
                return 0
            if q==0 and e==0 and b==1 and z==0:
                return 1
            if q==0 and e==0 and b==0 and z==1:
                return 0
        if surprising ==0:
            if b==1 or e==1:
                return 1
            return 0
    
    elif googlers==2:
        if surprising==2:
            if q==2 and e==0 and b==0 and z==0:
                return 2
            if q==0 and e==2 and b==0 and z==0:
                return 0
            if q==0 and e==0 and b==2 and z==0:
                return 2
            if q==0 and e==0 and b==0 and z==2:
                return 0
            
            if q==1 and e==1 and b==0 and z==0:
                return 1
            if q==1 and e==0 and b==1 and z==0:
                return 2
            if q==1 and e==0 and b==0 and z==1:
                return 1
            
            if q==0 and e==1 and b==1 and z==0:
                return 1
            if q==0 and e==1 and b==0 and z==1:
                return 0
            
            if q==0 and e==0 and b==1 and z==1:
                return 1
            
        if surprising==1:
            if q==2 and e==0 and b==0 and z==0:
                return 1
            if q==0 and e==2 and b==0 and z==0:
                return 0
            if q==0 and e==0 and b==2 and z==0:
                return 2
            if q==0 and e==0 and b==0 and z==2:
                return 0
            
            if q==1 and e==1 and b==0 and z==0:
                return 2
            if q==1 and e==0 and b==1 and z==0:
                return 2
            if q==1 and e==0 and b==0 and z==1:
                return 1
            
            if q==0 and e==1 and b==1 and z==0:
                return 2
            if q==0 and e==1 and b==0 and z==1:
                return 0
            
            if q==0 and e==0 and b==1 and z==1:
                return 1
            
        if surprising==0:
            return e+b
            
    elif googlers ==3:
        if surprising==0:
            return e+b
        if surprising==1:
            if q==3 and e==0 and b==0 and z==0:
                return 1
            if q==0 and e==3 and b==0 and z==0:
                return 0
            if q==0 and e==0 and b==3 and z==0:
                return 3
            if q==0 and e==0 and b==0 and z==3:
                return 0
            if q==2 and e==1 and b==0 and z==0:
                return 2
            if q==2 and e==0 and b==1 and z==0:
                return 2
            if q==2 and e==0 and b==0 and z==1:
                return 1
            if q==1 and e==2 and b==0 and z==0:
                return 3
            if q==1 and e==0 and b==2 and z==0:
                return 3
            if q==1 and e==0 and b==0 and z==2:
                return 1
            if q==0 and e==2 and b==1 and z==0:
                return 3
            if q==0 and e==2 and b==0 and z==1:
                return 0
            if q==0 and e==1 and b==2 and z==0:
                return 3
            if q==0 and e==1 and b==0 and z==2:
                return 0
            if q==0 and e==0 and b==2 and z==1:
                return 2
            if q==0 and e==0 and b==1 and z==2:
                return 1
            if q==1 and e==1 and b==1 and z==0:
                return 3
            if q==1 and e==1 and b==0 and z==1:
                return 2
            if q==1 and e==0 and b==1 and z==1:
                return 2
            if q==0 and e==1 and b==1 and z==1:
                return 2
            
            
        if surprising==2:
            if q==3 and e==0 and b==0 and z==0:
                return 2
            if q==0 and e==3 and b==0 and z==0:
                return 0
            if q==0 and e==0 and b==3 and z==0:
                return 3
            if q==0 and e==0 and b==0 and z==3:
                return 0
            if q==2 and e==1 and b==0 and z==0:
                return 3
            if q==2 and e==0 and b==1 and z==0:
                return 3
            if q==2 and e==0 and b==0 and z==1:
                return 2
            if q==1 and e==2 and b==0 and z==0:
                return 1
            if q==0 and e==2 and b==1 and z==0:
                return 1
            if q==0 and e==2 and b==0 and z==1:
                return 0
            if q==1 and e==0 and b==2 and z==0:
                return 3
            if q==0 and e==1 and b==2 and z==0:
                return 3
            if q==0 and e==0 and b==2 and z==1:
                return 2
            if q==1 and e==0 and b==0 and z==2:
                return 1
            if q==0 and e==1 and b==0 and z==2:
                return 0
            if q==0 and e==0 and b==1 and z==2:
                return 1
            if q==1 and e==1 and b==1 and z==0:
                return 3
            if q==1 and e==1 and b==0 and z==1:
                return 2
            if q==0 and e==1 and b==1 and z==1:
                return 1
            if q==1 and e==0 and b==1 and z==1:
                return 2
            
        if surprising ==3:
            if q==3 and e==0 and b==0 and z==0:
                return 3
            if q==0 and e==3 and b==0 and z==0:
                return 0
            if q==0 and e==0 and b==3 and z==0:
                return 3
            if q==0 and e==0 and b==0 and z==3:
                return 0
            if q==2 and e==1 and b==0 and z==0:
                return 0
            if q==2 and e==0 and b==1 and z==0:
                return 3
            if q==2 and e==0 and b==0 and z==1:
                return 2
            if q==1 and e==2 and b==0 and z==0:
                return 1
            if q==0 and e==2 and b==1 and z==0:
                return 1
            if q==0 and e==2 and b==0 and z==1:
                return 0
            if q==1 and e==0 and b==2 and z==0:
                return 3
            if q==0 and e==1 and b==2 and z==0:
                return 2
            if q==0 and e==0 and b==2 and z==1:
                return 2
            if q==1 and e==0 and b==0 and z==2:
                return 1
            if q==0 and e==1 and b==0 and z==2:
                return 0
            if q==0 and e==0 and b==1 and z==2:
                return 1
            if q==1 and e==1 and b==1 and z==0:
                return 2
            if q==1 and e==1 and b==0 and z==1:
                return 1
            if q==0 and e==1 and b==1 and z==1:
                return 1
            if q==1 and e==0 and b==1 and z==1:
                return 2
newFile = open("output.in","w")
caseNumber=1
for i in s[1:]:
    surprisingList=[]
    notsurprisingList=[]
    zlist=[]
    qlist=[]
    wlist = []
    elist=[]
    line = i
    q=0
    e=0
    t=0
    bothList=[]
    line = line.split()
    googlers = int(line[0])     ## N
    surprising = int(line[1])    ## S
    par = int(line[2])          ## p
    scores = line[3:]           ## scores of N
    newFile.writelines("Case #%s: "%(caseNumber),)
    for i in scores:
        try:
            nofnots = max(notSurprising[int(i)][1])
            nofs = max(surprisingNumbers[int(i)][1])
            if nofs>=par and nofnots>=par:
                #print 'a'
                bothList.append([surprisingNumbers[int(i)][1],notSurprising[int(i)][1]])
                t+=1
                #elist.append([surprisingNumbers[int(i)][1],notSurprising[int(i)][1]])
                #q+=1
                #e+=1
            elif nofs>=par and nofnots<par: #only surprising and not not surprising
                surprisingList.append(surprisingNumbers[int(i)][1])
                #qlist.append([surprisingNumbers[int(i)][1],notSurprising[int(i)][1]])
                #q+=1
            elif nofs<par and nofnots>=par:
                notsurprisingList.append(notSurprising[int(i)][1])
                #wlist.append([surprisingNumbers[int(i)][1],notSurprising[int(i)][1]])
            else:
                zlist.append(i)
                #zlist.append([surprisingNumbers[int(i)][1],notSurprising[int(i)][1]])
        except:
            #nofnots = max(notSurprising[int(i)][1])
            if nofnots>=par:
                notsurprisingList.append(notSurprising[int(i)][1])
            else:
                zlist.append(i)
                #elist.append([notSurprising[int(i)][1]])
    #print len(surprisingList),'x',len(notsurprisingList),'y',len(zlist),'z',len(zlist)>=surprising,t
    #print bothList
    #print caseNumber,len(zlist)>surprising,bothList
    #print surprisingList,notsurprisingList
    #if caseNumber==25:
    #    print googlers,surprising,len(surprisingList),len(notsurprisingList),len(bothList),len(zlist)
    #if len(zlist)==googlers:
        #newFile.writelines('0')
        #newFile.writelines("\n")
    #else:
        #print caseNumber
    newFile.writelines(str(outputList(googlers,surprising,len(surprisingList),len(notsurprisingList),len(bothList),len(zlist))))
    newFile.writelines("\n")
    caseNumber+=1
        
newFile.close()
