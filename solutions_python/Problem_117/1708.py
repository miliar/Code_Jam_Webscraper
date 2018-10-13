import time
import sys



def lm():
    data=readfile()
    numTestCase = data[0]
    data=data[1:]
    
    data=formatDat(data)
    #return data
    status=[0]*int(numTestCase)

    for i in range(int(numTestCase)):
        #print i
        status[i],data=checkPossible(data)
    
    writeFile(status)
    return  status
def checkPossible(data):
    size = data[0]
    print size
    data=data[1:]
    if(int(size[0])==1 or int(size[1])==1):
        data=data[int(size[0]):]
        return "YES",data
    
    for i in range(int(size[0])):
        for j in range(int(size[1])):
            #print "\n"
            if((checkRow(i,j,data,size)==True or checkCol(i,j,data,size)==True) or \
               (biggerThanSurrounding(i,j,data,size)==True) or \
               #(checkRow(i,j,data,size)==False and checkCol(i,j,data,size)==False and
                  (biggerThanROWCOL(i,j,data,size)==True)):
                #print str(i)+" "+str(j)
                pass
            else:
                print str(i)+" "+str(j) + " " + str(data[i][j])+"f"
                data=data[int(size[0]):]
                return "NO", data
    
    data=data[int(size[0]):]
    return "YES", data
def biggerThanSurrounding(i,j,data,size):
    print "S"
    top = i-1
    bot = i+1
    left = j-1
    right = j+1
    if top>=0:
         if data[i][j]>data[top][j]:
             return True
    if bot <= int(size[0])-1:
        if data[i][j]>data[bot][j]:
             return True
    if left >= 0:
        if data[i][j]>data[i][left]:
             return True
    if right <= int(size[1])-1:
        if data[i][j]>data[i][right]:
             return True
    return False
def biggerThanAllSurrounding(i,j,data,size):
    print "AS"
    top = i-1
    bot = i+1
    left = j-1
    right = j+1
    if top>=0:
         if data[i][j]<=data[top][j]:
             return False
    if bot <= int(size[0])-1:
        if data[i][j]<=data[bot][j]:
             return False
    if left >= 0:
        if data[i][j]<=data[i][left]:
             return False
    if right <= int(size[1])-1:
        if data[i][j]<=data[i][right]:
             return False
    return True
def biggerThanROWCOL(i,j,data,size):
    print "AS"
    top = i-1
    bot = i+1
    left = j-1
    right = j+1
    while((top<0 and bot > int(size[0])-1 and left < 0 and right > int(size[1])-1)!=True):
        #print (right > int(size[1])-1)
        if top>=0:
             if data[i][j]<data[top][j]:
                 return False
        if bot <= int(size[0])-1:
            if data[i][j]<data[bot][j]:
                 return False
        if left >= 0:
            if data[i][j]<data[i][left]:
                 return False
        if right <= int(size[1])-1:
            if data[i][j]<data[i][right]:
                 return False
        top = top-1
        bot = bot+1
        left = left-1
        right = right+1
    return True
def checkRow(i,j,data,size):
    #print "R"
##    if((i==0 and j==0 and (data[i][j]>=data[0][1] or data[i][j]>=data[1][0])) \
##       or (i==0 and j==int(size[1])-1 and (data[i][j]>=data[0][int(size[1])-2] or data[i][j]>=data[1][int(size[1])-2])) \
##       or (i==int(size[0])-1 and j==0 and (data[i][j]>=data[int(size[0])-2][0] or data[i][j]>=data[int(size[0])-1][1])) \
##       or (i==int(size[0])-1 and j==int(size[1])-1) and (data[i][j]>=data[int(size[0])-1][int(size[1])-2] or data[i][j]>=data[int(size[0])-2][int(size[1])-1])):
##        return True
    for k in range(len(data[i])-1):
        if data[i][k]!=data[i][k+1]:
            #print "Rfalse ", data[i][j]
            return False
    #print "Rtrue ", data[i][j]
    return True
def checkCol(i,j,data,size):
    #print "C"
##    if((i==0 and j==0 and (data[i][j]>=data[0][1] or data[i][j]>=data[1][0])) \
##       or (i==0 and j==int(size[1])-1 and (data[i][j]>=data[0][int(size[1])-2] or data[i][j]>=data[1][int(size[1])-2])) \
##       or (i==int(size[0])-1 and j==0 and (data[i][j]>=data[int(size[0])-2][0] or data[i][j]>=data[int(size[0])-1][1])) \
##       or (i==int(size[0])-1 and j==int(size[1])-1) and (data[i][j]>=data[int(size[0])-1][int(size[1])-2] or data[i][j]>=data[int(size[0])-2][int(size[1])-1])):
##        return True
    for k in range(int(size[0])-1):
        if data[k][j]!=data[k+1][j]:
            #print "Cfalse ", data[i][j]
            return False
    #print "Ctrue ", data[i][j]
    return True
def readfile():
    #fin = open("B-small-attempt5.in")
    fin = open("B-small-attempt11.in")
    data = fin.readlines()
    fin.close
    return data
def writeFile(status):
    fout = open("lm.out","w")
    for i in range(len(status)):
        fout.write('Case #'+str(i+1)+": "+str(status[i])+"\n")
    fout.close
    return status

def formatDat(data):
    for i in range(len(data)):
        data[i]=data[i].split()
            
    return data


    
st=time.time()
a=lm()
et=time.time()-st
print "done"
print et
