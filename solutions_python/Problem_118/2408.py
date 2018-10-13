import math

def isPal(n):
    s = str(n)
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1
    
    return j <= i

def isSqr(n):
    sqrtN = math.sqrt(n)
    
    sqrtNint = int(sqrtN)
    
    if float.is_integer(sqrtN) :
        
        return isPal(int(sqrtN))
    else:
        return False
    
fin = open("C-small-attempt0.in", "r")
fout = open("out.txt","w")

T = int(fin.readline())

for i in range(T):
    inputs = fin.readline()
    
    inputs = str.split(inputs," ")
    
    A = int(inputs[0])
    B = int(inputs[1])
    count = 0
    
    #for every integer in range
    for j in range(A,B+1):
    
        if (isPal(j) and isSqr(j)):
            count+=1
    fout.write("Case #"+str(i+1)+": "+str(count)+"\n")
    

fin.close()
fout.close()
