from string import *
import math

def read_words(filename):
    '''
    converts a file to a list
    '''
    
    words = []
    for line in filename:
            words.append(line.strip())
    return words

filename = open("Tim.txt", 'r')
numcases = int(filename.readline())

for case in range(numcases):
    numarray = (filename.readline().split())

    A = int(numarray[0])
    B = int(numarray[1])
    K = int(numarray[2])

    matchcount = 0
    for num in range(A):
        for num2 in range(B):
            if (num & num2 < K):
                matchcount+=1
                
    print "Case #" + str(case+1)+':', matchcount