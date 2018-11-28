import math

def isPalindrome(string):
    n = len(string)
    if n == 1:
        return True
    else :
        for i in range(0,n):
            if string[i] != string[n-i-1]:
                return False
    return True

def counting(rang,n):
    count = 0
    ceilSqRtL = int(math.ceil(math.sqrt(rang[0])))
    ceilSqRtH = int(math.floor(math.sqrt(rang[1])))               
    for i in range(ceilSqRtL,ceilSqRtH+1):
        if isPalindrome(str(i)):
            sq = i*i
            if isPalindrome(str(sq)):
                count+=1
    outputFile = open("output.txt",'a')
    outputFile.write('Case #'+ str(n) + ': ' + str(count)+ '\n')

            


filename = "C-small-attempt0.in"
inputFile = open(filename,'r')
outputFile = open("output.txt",'w')
outputFile.close()
i = 0
n = 0
for line in inputFile:
    if i == 0:
        i=1
        continue
    else:
        n+=1
        rang=[]
        temp = line.split(' ')
        for j in temp:
            j=j.split('\n')
            rang.append(int(j[0]))
        counting(rang,n)     
    i=i+1
    
inputFile.close()
            
            

inputFile.close()
