#problem A
T = input()
T = int(T)
for t in range(T):
    
    s = input()
    s = s.split(" ");
    sMax = s[0]
    sString = s[1]
    #print(s,sMax, sString)
    
    counter = 0
    current = int(sString[0])
    for index in range(len(sString)-1):
        while(current+counter < index+1):
            counter+=1
        current+= int(sString[index+1])
        
    print("Case #%d: %d"%(t+1, counter))
