import time
import sys
import math


def fns():
    data=readfile()
    numTestCase = data[0]
    data=data[1:]
    
    data=formatDat(data)
    #return data
    
    status=[0]*int(numTestCase)

    for i in range(int(numTestCase)):
        status[i],data=countFnS(data)
    
    writeFile(status)
    return  status
def countFnS(data):
    palCount=0
    sp=int(data[0][0])
    ep=int(data[0][1])
    for i in range(sp,ep+1):
        if(isPal(i)==True):
            if(math.sqrt(i)%1==0):
                if(isPal(int(math.sqrt(i)))==True):
                    #print str(math.sqrt(i))
                    palCount+=1
    data=data[1:]
    return palCount,data
def isPal(num):
    num=str(num)
    #print num
    while(len(num)>1):
        if(num[0]==num[len(num)-1]):
            num=num[1:len(num)-1]
        else:
            return False
    return True

def readfile():
    fin = open("C-small-attempt0.in")
    data = fin.readlines()
    fin.close
    return data
def writeFile(status):
    fout = open("fns.out","w")
    for i in range(len(status)):
        fout.write('Case #'+str(i+1)+": "+str(status[i])+"\n")
    fout.close
    return status

def formatDat(data):
    for i in range(len(data)):
        data[i]=data[i].split()
        #if len(data[i])!=0:
         #   data[i]=list(data[i][0])
            
    return data


st=time.time()
a=fns()
#a=isPal(44044)
et=time.time()-st
print "done"
print et
