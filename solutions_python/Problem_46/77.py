'''
Created on 2009/09/26

@author: hirobe
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self,params):
        '''
        Constructor
        '''

def test(datablock):
    #print datablock
    idata = []
    for st in datablock:
        l = len(st)
        t = False
        for i in range(0,l):
            if st[l-i-1] == '1':
                idata.append(l-i)
                t=True
                break
        if t==False:
            idata.append(0)
    #print idata
    ret = 0
    while(True):
        okLine = len(idata)-1
        for i in range(0,len(idata)-1):
            if idata[i]>i+1 :
                okLine = i
                #print "hoge %d"%(okLine)
                break
            
        #print okLine
        if okLine == len(idata)-1:
            #print "hoge2"
            break;
        for i in range(okLine,len(idata)):
            #print "%d %d %d"%(i,okLine,idata[i]) 
            #print idata
            if idata[i]<=okLine+1:
                #print "a%d %d"%(okLine,idata[i]) 
                hoge = idata[i-1]
                idata[i-1]= idata[i]
                idata[i] = hoge
                ret +=1
                break
    #print idata
    #print ret
    return ret
    pass

def read_file():
    data = []
    dataBlock = []
    isHead = True
    dataCount = 0
    blockCount = 0
    for line in open('A-large(2).in', 'r'):
        #print line
        if isHead:
            isHead = False
        elif dataCount ==0:
            dataCount = int(line.rstrip())
            if blockCount >0:
                data.append(dataBlock)
            dataBlock = []
            blockCount +=1
        else:
            dataBlock.append(line.rstrip())
            dataCount -=1
    data.append(dataBlock)
    #print data
    return data

hoge = read_file()

case_index = 1
#test(hoge[0])
#test(hoge[1])
for data in hoge:
    print "Case #%d: %d"%(case_index,test(data))
    case_index += 1