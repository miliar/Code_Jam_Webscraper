from math import ceil,floor

def isPalindrome(x):
    s = str(x)
    return s==s[::-1]
        
def palindromeGenerator(begin,end):
    for i in xrange(begin,end+1):
        if isPalindrome(i):
            yield(i)


# import

import sys
            
# MAIN

#For large inputs

maxValue = 1e14
listFairAndSquare=[]

for palindrome in palindromeGenerator(int(ceil(1**0.5)),int(floor(1e14**0.5))):
	if isPalindrome(palindrome**2):
		listFairAndSquare.append(palindrome**2)


inFile=open(sys.argv[1],'r')
outFile = open(sys.argv[2],'w')

numCases = int(inFile.readline())

for i in xrange(numCases):

    (begin,end) = map(int,inFile.readline().rstrip().split())

    fairAndSquareCount = sum([(end>=number and number >= begin) for number in listFairAndSquare])

    print fairAndSquareCount

    outFile.write('Case #{}: {}\n'.format(i+1,fairAndSquareCount))


    
