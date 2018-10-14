##def extractNumber( digits ):
##    string = ""
##    for item in digits:
##        string += str(item)
##    return int(string)
##
##def generateAllPalindromes( numDigits):
##    palindromes = []
##    if numDigits % 2 == 0: #even
##        half = numDigits / 2
##        digits = [0]*half
##        digits[0] = 1
##        while(True):
##            palindromes.append(extractNumber( digits))
##            digits[half-1]+=1 #inc the last one by 1
##            if digits[half-1] == 10: #inc next one
##                index = half-2
##                while True:
##                    if index<0: 
##                        return palindromes
##                    digits[index+1] = 0
##                    digits[index]+=1
##                    if digits[index]!=10:
##                        break
##                    index-=1

import math

##ALLPALI = []
##for a in range(1, 8):
##    ALLPALI+=generateAllPalindromes(numDigits)
    
def ispali(num):
    return str(num) == str(num)[::-1]

def generateAllPalindromes( numDigits):
    palindromes = []
    if numDigits % 2 ==0:
        half = numDigits / 2
        start = 10**(half-1)
        end = 10**(half)
        for a in range(start, end):
            palindromes.append(int(str(a)+str(a)[::-1]))
    else: #treat as even 1 shorter, then add in the middle
        half = numDigits / 2
        start = int( 10**(half-1))
        if start==0:
            return [1,2,3,4,5,6,7,8,9]
        end = 10**half
        #print start, end
        for a in range(start,end):
            for b in range(10):
                palindromes.append( int( str(a)+str(b)+str(a)[::-1]))
    return palindromes

def numPali(lower, upper):
    lownumdigits = int( math.log(lower, 10) ) + 1
    highnumdigits = int( math.log(upper,10) ) + 1
    allpali = []
    for a in range(lownumdigits, highnumdigits+1):
        allpali+= generateAllPalindromes(a)
    
    total = 0
    for pali in allpali:
        if pali >= lower and pali <= upper and ispali(pali**2):
            total+=1
    return total

##def numpalifast(lower,upper):
##    total = 0
##    for pali in ALLPALI:
##        if pali > upper:
##            break
##        if pali >= lower and ispali(pali**2):





##def getAll(lower, upper):
##    total = 0
##    for a in range(int(lower), int(upper+1)):
##        if ispalin(a) and ispalin(a**2):
##            total+=1
##    return total

data = [line.strip() for line in open("input.txt")]
output = []
count = 0
for item in data[1:]:
    count+=1
    print count
    line = [int(token) for token in item.split()]
    lower = math.ceil(line[0]**.5)
    upper = math.floor(line[1]**.5)
    output.append(numPali(lower, upper))

print output
f = open("output.txt", 'w')
for i in range(len(output)):
    f.write("Case #"+str(i+1)+": "+str(output[i])+"\n")
f.close()
