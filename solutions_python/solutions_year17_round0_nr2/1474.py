def Decrement(index,numStr):
    numStr[index]=str(int(numStr[index])-1) #Lower the number, and fill the rest with nines if we're not coming from front
    for i in range(index+1,len(numStr)): numStr[i]='9'
    
    if(index==0 and numStr[index]=='0'): #If we're at the beginning of the str, we're done
        for i in range(len(numStr)-1): numStr[i]='9'
        numStr.pop()
        
           
    #Maybe we just violated the property backwards, decrement the guy behind us
    if(index>0 and int(numStr[index-1])>int(numStr[index])): Decrement(index-1,numStr)
           
           
def Ans(numStr):
    numStr=list(numStr)
    for index in range(len(numStr)):
        if(index==len(numStr)-1): break
        if(int(numStr[index])>int(numStr[index+1])): #Find the point where the property is violated
            Decrement(index,numStr)
            return numStr
            
    return numStr
                   

numCases=int(raw_input())

for case in range(numCases):
    inputStr=raw_input()
    print ("Case #"+str(case+1)+": "+"".join(Ans(inputStr)))

    
