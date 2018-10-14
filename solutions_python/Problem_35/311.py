fin = open("b.in","r")
fout = open("b.out","w")
num = 0
h = 0
w = 0
data = []
data2 = []
line = ""
sinkCount = 0
current = 96
c = chr(96)
#-----------------------------
def getMin(mincells,value):
    global sinkCount
    #print mincells
    minVal = max(mincells)+1
    minInd = 5
    for i in range(0,4):
        if mincells[i] != -1 and mincells[i] < minVal:
            minVal = mincells[i]
            minInd = i
    if (value <= minVal):
        sinkCount+=1
        return 'B' 
    if (minInd == 0):return 'N'
    if (minInd == 1):return 'W'
    if (minInd == 2):return 'E'
    if (minInd == 3):return 'S'


def label(i,j):
    global data2,current
    global c
    if data2[i][j] == 'N':   label(i-1,j)
    elif data2[i][j] == 'W': label(i,j-1)
    elif data2[i][j] == 'E': label(i,j+1)
    elif data2[i][j] == 'S': label(i+1,j)
    elif data2[i][j] == 'B':
        current+=1
        data2[i][j] = chr(current)
        c = chr(current)
    else:
        c = data2[i][j]
    data2[i][j] = c
    
        
    
        
def calc():
    global data,data2,h,w
    for i in range(0,h):
        for j in range(0,w):
            mincells = []
            if i > 0: mincells.append(data[i-1][j])
            else: mincells.append(-1)
            if j > 0: mincells.append(data[i][j-1])
            else: mincells.append(-1)
            if j < w-1: mincells.append(data[i][j+1])
            else: mincells.append(-1)            
            if i < h-1: mincells.append(data[i+1][j])
            else: mincells.append(-1)
            #print i,j,mincells,getMin(mincells,data[i][j])
            data2[i][j] = getMin(mincells,data[i][j])
    #print data2
    for i in range(0,h):
       for j in range(0,w):
           if data2[i][j] == 'N' or data2[i][j] == 'S' or data2[i][j] == 'W' or data2[i][j] == 'E' or data2[i][j] == 'B':
               #print i,j
               label(i,j)
               #print data2
    #print "sink count " , sinkCount    
#------------------------------------------------------------------
num = int(fin.readline()[:-1])

for i in range(0,num):
    #if (i > 1):
     #   continue
    fout.write("Case #" + str(i+1) + ":\n")
    line = fin.readline()
    h = int(line.split()[0])
    w = int(line.split()[1])
    data = [[0] * w] * h
    data2 = []
    current = 96
    sinkCount = 0
    for j in range(0,h):
        data2.append([0]*w)
        
    for j in range(0,h):
        line = fin.readline().split()
        data[j]= [int(r) for r in line]
    #print data
    if h == w == 1:
        data2 = ['a']
    else:
        calc()
    '''
    print "case " + str(i)
    for k in data:
        print k
    print "---------------------------"
    for k in data2:
        print k
    print "----------------------------"
    ppp = raw_input()
    '''
    
    for j in range(0,h):
        for k in range(0,w-1):
            fout.write(data2[j][k] + " ")
        fout.write(str(data2[j][w-1]) + "\n")
    

fin.close()
fout.close()
