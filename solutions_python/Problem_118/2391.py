import math

def isWhole(n):
    return(n%1 == 0)

def isFairNSquare(n):
    s = math.sqrt(int(n))
    
    if not isWhole(s):    
        return False
    
    fair = True
    s = str(int(s))
    for i in range(len(n)//2):
        if n[i] != n[i*-1]:
            fair = False
            
    if not fair: return fair
    for i in range(len(s)//2):
        if s[i] != s[i*-1]:
            fair = False        
            
    return fair

#num = int(input())
#for case in range(num):
    #line = input()

isFairNSquare("100")