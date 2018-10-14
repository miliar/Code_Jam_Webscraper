import sys
import string
import operator
import math
import re

# globals
infile = ''
N = 0
L=0
D=0
dict = []
output = []
debug = False

def processCase(i):
    global infile, currentLine, debug
    if debug:
        print '### processing case '+str(i+1)
    
    # read data
    pattern = infile[currentLine]
    currentLine += 1
    
    ## solve the problem
    nMatch = 0
    pattern = pattern.replace('(', '[')
    pattern = pattern.replace(')',']')
    p = re.compile(pattern)
    for w in dict:
        if re.match(p, w):
            nMatch += 1
        
    return nMatch


# apply a function to a list
def map( fun, list ):
    nlist = []
    for item in list:
        nlist.append( fun( item ) )
    return nlist

    
# Main procedure
infileName = sys.argv[1]
infile = open(infileName, 'r').readlines()
[L,D,N]=map(int,infile[0].split())
currentLine = 1
#print L,D,N
for i in range(D):
    dict.append(infile[currentLine])
    currentLine+=1

output = []
for i in range(N):
    result = processCase(i)
    output.append(result)
    
for i,v in enumerate(output):
    print 'Case #'+str(i+1)+':',v
    