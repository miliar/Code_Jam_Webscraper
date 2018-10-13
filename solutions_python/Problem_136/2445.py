from sys import argv
script, ipfile = argv





def getSolution(C, F, X):
    
    currentF = 2.0
    prevF = 2.0
    currentTime = X/2.0 
    prevT = 0

    while(1 == 1):
        
        currentF = currentF + F

        withC = prevT + (C/prevF) + (X/currentF)
 

        if(withC < currentTime):
            currentTime = withC
            prevT = prevT + (C/prevF)
            prevF = currentF

        else:
            return currentTime



ip = open(ipfile,'r')

readip = ip.read()
readip = readip.split('\n')


testcases = int(readip[0])



cnt = 1
i = 1

while (cnt <= testcases):

    current_time = 0
    prev_time = 0

    get_row = readip[i].split()    
    
    C = float(get_row[0])
    F = float(get_row[1])
    X = float(get_row[2])

    i = i+1

    result = getSolution(C,F,X)
    
    print "Case #%d: %.7f" %(cnt,result)
    
    cnt = cnt + 1



    
ip.close

 
