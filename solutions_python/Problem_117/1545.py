'''
Created on 03/04/2013

@author: Jamie Williamson 
'''

import time
import sys
import logging
     
'''
Main Code 
'''
def run():
    
    testCases = int(nextline())

    for t in range(1, testCases+1):

        N, M = map(int, nextline().split())

        # Fill the 2D array 
        array = []
        for n in range(0, N):
            array.append(map(int, nextline().split()))

        # Scan the array for impossible scenarios 
        possible = "YES"
        for i in range(0, N):
            foundLeftRight = False
            foundUpDown = False
            indexUpDown = -1
            indexLeftRight = -1
            for j in range(0, M):
                # Check to up and down and mark if bigger number exists 
                for y in range(0, N):
                    if array[y][j] > array[i][j]:
                        foundUpDown = True
                        indexUpDown = y
                        break

                # Check to right and left and mark if bigger number exists 
                for x in range(0, M):
                    if array[i][x] > array[i][j]:
                        foundLeftRight = True
                        indexLeftRight = x
                        break

                # If both, impossible, break 
                if foundLeftRight and foundUpDown:
                    possible = "NO"
                    # print "Case %d Found impossible at %d,%d with items %d,%d" % (t, i, j, indexUpDown, indexLeftRight)
                    break
            if possible == "NO":
                break

        print 'Case #%s:' %t, possible
    
    return 

'''
Helper Functions 
'''

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
        








