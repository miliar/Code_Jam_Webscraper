#!/usr/bin/env python
import math
import sys

def isPalindrome(n):
    numString = str(n)
    length = len(numString)
    for i in range(length/2):
        if (numString[i] != numString[-(i+1)]):
            return False
    return True

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

lines = fin.readlines()
index = int(lines.pop(0).rstrip())

for n in range(index):
    #read data
    limit = lines.pop(0).rstrip().split()
    a = int(limit[0])
    b = int(limit[1])
    sa = int(math.ceil(math.sqrt(a)))
    sb = int(math.floor(math.sqrt(b)))

    print 'range : [' + str(sa) + ' - ' + str(sb) + ']'

	#look for possible value
    count = 0
    for i in range(sa, sb+1):
        # print 'i : ' + str(i)
        if (isPalindrome(i)):
            square = i * i
            # print 'square : ' + str(square)
            if (isPalindrome(square)):
                count = count + 1
                print 'found one : ' + str(i) + ' <> ' + str(square)
    
    print 'total = ' + str(count)
    fout.write('Case #' + str(n+1) + ': ' + str(count))	
    fout.write('\n')
    # lines.pop(0) #skip empty line

fout.close()