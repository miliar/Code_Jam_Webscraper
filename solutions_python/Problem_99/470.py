'''
Created on 2012/4/28

@author: 13k
'''
def read_input(fileName):
    f = open(fileName,"r")
    data    = []
    while True:
        line    = f.readline()
        
        if len(line) == 0:
            break
        data.append(line)
    return data
def refineData(rawData):
    dataList    = []
    for i in range(0,len(rawData)):
        dataList.append(rawData[i].split())
    return dataList
def refineData_float(rawData):
    dataList    = []
    for i in range(0,len(rawData)):
        #dataList.append(rawData[i].split())
        dataList.append(list(map(float,rawData[i].split())))
    return dataList
def tree(numLt,num,count):
    if count<=0:
        resultLt.append(num)
    else:
        
        tree(numLt[1:],num*numLt[0],count-1)
        tree(numLt[1:],num*(1-numLt[0]),count-1)
if __name__ == '__main__':
    rawData = [ "3",
                "2 5",
                "0.6 0.6",
                "1 20",
                "1",
                "3 4",
                "1 0.9 0.1"
               ]
    rawData = read_input("c:\\A-small-attempt0.in")
    data    = refineData_float(rawData)
    #print(data)
    caseNum = int(data.pop(0)[0])
    
    for i in range(caseNum):
        print("Case #%d: " % (i+1),end = "")
        tmpLt   = data.pop(0)
        
        aNum    = tmpLt[0]
        bNum    = tmpLt[1]
        numberLt= data.pop(0)
        resultLt= []
        tree(numberLt,1,aNum)
             
        #print(resultLt)
        
        result  = []
        for j in range(int(aNum+1)):
            result.append(0)
            for i in range(len(resultLt)):
                if i < (2**j):
                    result[j]+=((bNum - aNum +1+j*2)*resultLt[i])
                else:
                    result[j]+=((2*bNum - aNum +2+j*2)*resultLt[i])
        
        result.append(bNum+2)
        result.sort(key=None, reverse=False)
        print("%.6f" % result[0])
        
        
        #for i in range(int(aNum)):
            
        
        
        
        
        
        
        """
        for i in range(int(aNum)):
            for j in range(2**i):
                result.append((bNum*2-aNum+2+i*2)*resultLt.pop(0))
        print(result)
        """