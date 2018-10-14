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

        # Build a 2D array of items 
        N = 4 # 4x4 board 
        items = [['.' for i in range(N)] for j in range(N)]
        for n in range(0, N):
            items[n] = list(nextline())

        # Skip the blank line 
        blank = nextline()

        # Check for K-in-a-row's 
        K = 4 # Need 4 in a row 
        foundO = False
        foundX = False
        for i in range(0, N):
            for j in range(0, N):
                if(items[i][j] != '.'):
                    # Look k places down
                    found = True
                    for k in range(0, K):
                        if i+k >= len(items):
                            found = False
                            break
                        elif items[i][j] == 'T':
                            if i+1 < len(items) and items[i+k][j] != items[i+1][j] and items[i+k][j] != 'T':
                                found = False
                                break;
                        elif items[i+k][j] != items[i][j] and items[i+k][j] != 'T':
                            found = False
                            break
                    if found and items[i][j] == 'O':
                        foundO = True
                    if found and items[i][j] == 'X':
                        foundX = True
                    if found and items[i][j] == 'T':
                        if items[i+1][j] == 'O':
                            foundO = True 
                        if items[i+1][j] == 'X':
                            foundX = True

                    # Look k places right
                    found = True
                    for k in range(0, K):
                        if j+k >= len(items):
                            found = False
                            break
                        elif items[i][j] == 'T':
                            if j+1 < len(items[i]) and items[i][j+k] != items[i][j+1] and items[i][j+k] != 'T':
                                found = False
                                break;
                        elif items[i][j+k] != items[i][j] and items[i][j+k] != 'T':
                            found = False
                            break
                    if found and items[i][j] == 'O':
                        foundO = True
                    if found and items[i][j] == 'X':
                        foundX = True
                    if found and items[i][j] == 'T':
                        if items[i][j+1] == 'O':
                            foundO = True 
                        if items[i][j+1] == 'X':
                            foundX = True

                    # Look k places diagonally down-right
                    found = True
                    for k in range(0, K):
                        if i+k >= len(items) or j+k >= len(items):
                            found = False
                            break
                        elif items[i][j] == 'T':
                            if i+1 < len(items) and j+1 < len(items[i]) and items[i+k][j+k] != items[i+1][j+1] and items[i+k][j+k] != 'T':
                                found = False
                                break;
                        elif items[i+k][j+k] != items[i][j] and items[i+k][j+k] != 'T':
                            found = False
                            break
                    if found and items[i][j] == 'O':
                        foundO = True
                    if found and items[i][j] == 'X':
                        foundX = True
                    if found and items[i][j] == 'T':
                        if items[i+1][j+1] == 'O':
                            foundO = True 
                        if items[i+1][j+1] == 'X':
                            foundX = True

                    # Look k places diagonally down-left
                    found = True
                    for k in range(0, K):
                        if i+k >= len(items) or j-k < 0:
                            found = False
                            break
                        elif items[i][j] == 'T':
                            if i+1 < len(items) and j-1 >= 0 and items[i+k][j-k] != items[i+1][j-1] and items[i+k][j-k] != 'T':
                                found = False
                                break;
                        elif items[i+k][j-k] != items[i][j] and items[i+k][j-k] != 'T':
                            found = False
                            break
                    if found and items[i][j] == 'O':
                        foundO = True
                    if found and items[i][j] == 'X':
                        foundX = True
                    if found and items[i][j] == 'T':
                        if items[i+1][j-1] == 'O':
                            foundO = True 
                        if items[i+1][j-1] == 'X':
                            foundX = True

        # print foundO, ' ', foundX

        if not foundO and not foundX:
            for i in range(0, K):
                for j in range(0, K):
                    if items[i][j] == '.':
                        foundO = True
                        foundX = True
                        break;
                if foundO and foundX:
                    break;

        results = ['Draw', 'O won', 'X won', 'Game has not completed']
        result = results[foundO + foundX*2]

        print 'Case #%s:' %t, result
    
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
    infname = problemletter + '-large.in'
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
        








