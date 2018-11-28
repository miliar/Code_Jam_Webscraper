import sys;
import math;
import re;

def isPalindrome(num):
    numStr = str(num)
    numRever = numStr[::-1]
    if numRever == numStr:
        return 1
    else:
        return 0
        
def isPerfectSquare(num):
    sqr = math.sqrt(num) 
    sqrStr = str(sqr)
    if re.match("^\d+\.0{1}$",sqrStr):
        return int(sqr)
    else:
        return None

if len(sys.argv) > 1:
    file = open(sys.argv[1],'r')
    T = int(file.readline().replace('\n',''))
    for t in range(1,T+1):
        count = 0
        rango = file.readline().replace('\n','')
        rango = rango.split(' ')
        A = int(rango[0])
        B = int(rango[1])
        #recorro el rango del test
        for r in range(A,B+1):
            if isPalindrome(r): #si es palindrome
                sqr = isPerfectSquare(r)
                if sqr: #si es cuadrado perfecto
                    if isPalindrome(sqr): #si su cuadrado tambien es palindrome
                        count += 1
        print("Case #" + str(t) + ": " + str(count)) 
                    
else:
    print("You must give me a file")
