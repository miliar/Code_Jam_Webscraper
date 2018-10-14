import time
import sys

XWins="X won"
OWins="O won"

def ttt():
    data=readfile()
    numTestCase = data[0]
    data=data[1:]
    
    data=formatDat(data)
    
    for i in data:
        print i;
    
    
    status=[0]*int(numTestCase)

    for i in range(int(numTestCase)):
        status[i],data=checkWinStatus(data)
        if status[i]==False:
            checkDraw(data)
    
    writeFile(status)
    return  status

def checkWinStatus(data):
    status=False
##    for j in range(4):
##            for k in range(4):
##                #print "hi"
    if(checkRow(data)==XWins):
       status=XWins
    elif(checkRow(data)==OWins):
        status=OWins
    if(checkCol(data)==XWins):
       status=XWins
    elif(checkCol(data)==OWins):
        status=OWins
    if(checkDiag(data)==XWins):
       status=XWins
    elif(checkDiag(data)==OWins):
        status=OWins
    if status == False:
        status=checkDraw(data)
    data=data[5:]
    return status,data
def checkDraw(data):
    status=False
    for i in range(4):
        for j in range(4):
            if data[i][j]=='.':
                status="Game has not completed"
                return status
            else:
                status="Draw"
    return status
def checkRow(data):

    anyoneWin=True
    for j in range(4):
           if data[j][0]=='X' or data[j][0]=='T':
               if data[j][1]=='X' or data[j][1]=='T':
                   if data[j][2]=='X' or data[j][2]=='T':
                       if data[j][3]=='X' or data[j][3]=='T':
                           #print "X winner"
                           return XWins
    for j in range(4):
           if data[j][0]=='O' or data[j][0]=='T':
               if data[j][1]=='O' or data[j][1]=='T':
                   if data[j][2]=='O' or data[j][2]=='T':
                       if data[j][3]=='O' or data[j][3]=='T':
                           #print "O winner"
                           return OWins
    #print "no winner"
    return False
def checkCol(data):

    anyoneWin=True
    for k in range(4):
           if data[0][k]=='X' or data[0][k]=='T':
               if data[1][k]=='X' or data[1][k]=='T':
                   if data[2][k]=='X' or data[3][k]=='T':
                       if data[3][k]=='X' or data[3][k]=='T':
                           #print "X winner"
                           return XWins
    for k in range(4):
           if data[0][k]=='O' or data[0][k]=='T':
               if data[1][k]=='O' or data[1][k]=='T':
                   if data[2][k]=='O' or data[2][k]=='T':
                       if data[3][k]=='O' or data[3][k]=='T':
                          # print "O winner"
                           return OWins
    #print "no winner"
    return False
def checkDiag(data):

    anyoneWin=True
    
    if data[0][0]=='X' or data[0][0]=='T':
        if data[1][1]=='X' or data[1][1]=='T':
            if data[2][2]=='X' or data[2][2]=='T':
                if data[3][3]=='X' or data[3][3]=='T':
                      #print "X winner"
                    return XWins
    if data[0][3]=='X' or data[0][3]=='T':
        if data[1][2]=='X' or data[1][2]=='T':
            if data[2][1]=='X' or data[2][1]=='T':
                if data[3][0]=='X' or data[3][0]=='T':
                      #print "X winner"
                    return XWins
    if data[0][0]=='O' or data[0][0]=='T':
        if data[1][1]=='O' or data[1][1]=='T':
            if data[2][2]=='O' or data[3][2]=='T':
                if data[3][3]=='O' or data[3][3]=='T':
                          # print "O winner"
                    return OWins
    if data[0][3]=='O' or data[0][3]=='T':
        if data[1][2]=='O' or data[1][2]=='T':
            if data[2][1]=='O' or data[2][1]=='T':
                if data[3][0]=='O' or data[3][0]=='T':
                          # print "O winner"
                    return OWins
    #print "no winner"
    return False
                
def readfile():
    fin = open("A-small-attempt3.in")
    data = fin.readlines()
    fin.close
    return data
def writeFile(status):
    fout = open("ttt.txt","w")
    for i in range(len(status)):
        fout.write('Case #'+str(i+1)+": "+str(status[i])+"\n")
    fout.close
    return status

def formatDat(data):
    for i in range(len(data)):
        data[i]=data[i].split()
        if len(data[i])!=0:
            data[i]=list(data[i][0])
            
    return data

def mergesort(data):
    
    if len(data)==1:
        return data
    mid=(len(data))/2
    return merge(mergesort(data[:mid]),mergesort(data[mid:]))
def merge(data1,data2):
    data=[]
    for i in range(len(data1)+len(data2)):
        if len(data1)==0:
            for j in data2:
                data.append(j)
            return data
        if len(data2)==0:
            for j in data1:
                data.append(j)
            return data
        
        #print data1[0],data2[0]
        if len(data1[0])<len(data2[0]):
            data.append(data2[0])
            data2=data2[1:]
        elif len(data1[0])>len(data2[0]):
            data.append(data1[0])
            data1=data1[1:]
        elif len(data1[0])==len(data2[0]):
            data.append(data1[0])
            data1=data1[1:]  
    return data
    
st=time.time()
a=ttt()
et=time.time()-st
print "done"
print et
