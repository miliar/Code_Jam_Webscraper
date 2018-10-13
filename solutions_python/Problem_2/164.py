import string

nmax = 100
namax = 100
nbmax = 100
tmax = 60

arrayAd = []
arrayAa = []
arrayBd = []
arrayBa = []
arrayAflag = []
arrayBflag = []

for i in range(0,namax):
    arrayAd.append(0)
    arrayBa.append(0)
    arrayAflag.append(0)    
for i in range(0,nbmax):
    arrayBd.append(0)
    arrayAa.append(0)
    arrayBflag.append(0)
    
def sortArray(ar,n):
    for i in range(0,n):
        for j in range(i,n):
            if ar[j] < ar[i]:
                ar[i], ar[j] = ar[j], ar[i]    
    
f = open('C:\\Users\\Moose\\workspace\\train\\B-large.in','r')
nbCases = int(f.readline())
for caseNb in range(0,nbCases):
    reduceDepartTrainB = 0
    reduceDepartTrainA = 0
    t = int(f.readline())
    na, nb = string.split(f.readline()," ")
    na = int(na)
    nb = int(nb)
    for i in range(0,na):
        temp1, temp2 = string.split(string.strip(f.readline())," ")
        temp1a, temp1b = string.split(temp1,":")
        arrayAd[i] = int(temp1a)*60+int(temp1b)
        temp2a, temp2b = string.split(temp2,":")
        arrayBa[i] = int(temp2a)*60+int(temp2b)+t
        arrayAflag[i] = 0
    for i in range(0,nb):
        temp1, temp2 = string.split(string.strip(f.readline())," ")
        temp1a, temp1b = string.split(temp1,":")
        arrayBd[i] = int(temp1a)*60+int(temp1b)
        temp2a, temp2b = string.split(temp2,":")
        arrayAa[i] = int(temp2a)*60+int(temp2b)+t
        arrayBflag[i]=0
        
    sortArray(arrayAd,na)
    sortArray(arrayBa,na)
    sortArray(arrayBd,nb)
    sortArray(arrayAa,nb)
    
    for i in range(0,na):
        for j in range(0,nb):
            if (arrayBa[i] <= arrayBd[j]) and (arrayBflag[j] == 0):
                arrayBflag[j] = 1
                reduceDepartTrainB += 1
                break
            
    for i in range(0,nb):
        for j in range(0,na):
            if (arrayAa[i] <= arrayAd[j]) and (arrayAflag[j] == 0):
                arrayAflag[j] = 1
                reduceDepartTrainA += 1
                break
                
    print "Case #" + str(caseNb+1) + ": " + str(na-reduceDepartTrainA) + " " + str(nb-reduceDepartTrainB)

f.close()        