
def getArray(number):
    result=[]
    while(number!=0):
        result.append(number%10)
        number=number//10
    return result

def getValue(arr):
    mul=1
    result=0
    for i in arr:
        result+=i*mul
        mul*=10
    return result

def checkTidy(arr):
    for i in range(0,len(arr)-1):
        if(arr[i]<arr[i+1]):
            return False
    return True

def temp(number):
    while(not checkTidy(getArray(number))):
        number-=1
    return number

def findUTidy(number):
    nArray=getArray(number)
    n=len(nArray)
    #print(nArray)
    if(n==1):
        return number
    cIndex=0
    mc=-1
    while(cIndex!=-1):
        cIndex=-1
        for i in range(0,n-1):
            if (nArray[i]<nArray[i+1]):
                nArray[i]=9
                cIndex=i+1
                if(mc<cIndex):
                    nArray[cIndex]=nArray[cIndex]-1
                    mc=cIndex
                break
    result=getValue(nArray)
    return result

t= int(input())
for i in range(0,t):
    n=int(input())
    print('Case #{}: {}'.format(i+1,findUTidy(n)))
