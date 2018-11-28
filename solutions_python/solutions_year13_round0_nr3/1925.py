'''
Created on 03/04/2013

@author: Jamie Williamson 
'''

import time
import sys
import logging
import math 
     
'''
Main Code 
'''
def run():
    
    testCases = int(nextline())

    for t in range(1, testCases+1):

        A, B = map(int, nextline().split())

        count = 0
        s = 0
        start = int(math.floor(math.sqrt(A)))
        for a in range(start, B+1):
            if palindrome(a):
                s = a*a
                if s > B:
                    break
                elif palindrome(s) and s >= A:
                    count += 1

        print 'Case #%s:' %t, count
    
    return 

'''
Helper Functions 
'''
def palindrome(n):
    
    n = str(n)
    for x in range(int(math.ceil(len(n)/2))):
        if n[x] != n[len(n) - 1 - x]:
            return False
    
    return True


'''
Main Function 
'''
def main():
    #s = time.time()
    run() 
    #print "Completed in", time.time() - s, "seconds"  


'''
Call main  
'''
#if __name__ == '__main__':

# Work out input and output file names
if len(sys.argv) > 1:
    sampledata = False
    infname = sys.argv[1]
else:
    sampledata = True
    scriptname = sys.argv[0]
    problemletter = scriptname[:scriptname.index('.')]
    infname = problemletter + '-small.in'
outfname = infname[:infname.index('.')] + '.out'

# Set up input
with open(infname) as f:
    text = f.read()
lines = text.splitlines()
linesiter = iter(lines)
nextline = linesiter.next

# Set up output
ofile = open(outfname, 'w')
sys.stdout = ofile


# Excecute main 
main()


#####################
# Template code below
#####################

sys.stdout = sys.__stdout__
ofile.close()
if sampledata:
    base = problemletter+'-example.'
    outfile = base+'out'
    rightfile = base+'right'
    out = open(outfile).read()
    right = open(rightfile).read()
    if out==right:
        print 'Congrats, your output matches sample output'
    else:
        print 'OUTPUT MISMATCH'
        








