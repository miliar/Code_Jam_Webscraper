import math
nTest = int(raw_input())

def isPalin(s):
    return (not s) or (s[0]==s[-1] and isPalin(s[1:-1])) 

def isSqrofPalin(n):
    sqrt =  math.sqrt(n)
    if sqrt.is_integer():
        sqrt = int(sqrt)
        #print str(sqrt)+": is perfect square"
        if isPalin(str(sqrt)):
            return True
    return False

for iTest in range(nTest):
    data = map(int,raw_input().split())
    a,b = data[0],data[1]
    
    count = 0
    
    for i in range(a,b+1):
        
        if isPalin(str(i)): 
            #print str(i)+": is palin"
            if isSqrofPalin(i):
                count += 1
    
    print "Case #"+str(iTest+1)+": "+str(count)