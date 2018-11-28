#!/usr/bin/python
# Filename: snapperchain.py

'''
Created on May 8, 2010

@author: zeest
'''

'''
NOTES: Files must have \n as separator

'''


'''

Problem Statement: Snapper Chain

Problem

The Snapper is a clever little gadget that, on one side, plugs into a power socket and, on the other side, exposes a power socket for plugging in a light or other device.

When the Snapper is in the ON state and is receiving power from the input socket, 
then the connected device is receiving power as well. When you snap your fingers, 
the Snapper toggles between the ON and OFF states. 
Of course, snapping your fingers only has an effect if the Snapper is plugged in and is receiving power from the socket.

In hopes of destroying the universe by means of a singularity, 
I have purchased N Snapper devices and chained them together by plugging the first one into a power socket, 
the second one into the first one, and so on. The light is plugged into the Nth Snapper.

Initially, all the Snappers are in the OFF state, so only the first one is receiving power from the socket, 
and the light is off. I snap my fingers once, which toggles the first Snapper into 
the ON state and gives power to the second one. I snap my fingers again, 
which toggles both Snappers and then promptly cuts power off from the second one, 
leaving it in the ON state, but with no power. I snap my fingers the third time, which toggles the first 
Snapper again and gives power to the second one. Now both Snappers are in the ON state, 
and if my light is plugged into the second Snapper it will be on.

I keep doing this for hours. Will the light be on or off after I have snapped my fingers K times? 
The light is on if and only if it's receiving power from the Snapper it's plugged into.

Input

The first line of the input gives the number of test cases, T. T lines follow. Each one contains two integers, N and K.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) 
and y is either "ON" or "OFF", indicating the state of the light bulb.

Limits

1 <= T <= 10,000.

Small dataset

1 <= N <= 10;
0 <= K <= 100;

Large dataset

1 <= N <= 30;
0 <= K <= 10^8;

Sample

 
Input
 
4
1 0
1 1
4 0
4 47

Output

Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON
 
@ Google Code Jam 2010
@ Link: http://code.google.com/codejam/contest
'''


#imports
from myFileIO import readFromFile, writeToFile

# File Paths

example1_in = 'example.in'
example1_out = 'example.out'

DEBUG = False
ASKFORFILE = True

def snapper (inputFile, outputFile):    
    ''' Solves Snapper Chain example.
    
    Elegantly '''
   
    fOK = True
    base = 2L
    power = 0L
    onvalue = 0L
    
    data = []
    results = []
    
    # read values
    data = readFromFile(inputFile)
    
    if len(data) <= 0:
        fOK = False
        
    if fOK:    
        TCases = int(data [0][0])
    
            
        if DEBUG:
            print data
            print TCases
            
        # loop on test cases
        for t in range (0, TCases):
                tS = 1+t
                Ndevices = long(data [tS][0])
                Ksnaps = long(data [tS][1])
                              
                if DEBUG:
                    print 'Case: ' + str(t) + '\tDevices: ' + str(Ndevices) + '\tSnaps: ' + str(Ksnaps)

                # After solving on paper for N lamps where N = 1, 2, 3 ,4, it was clear that snaps done K times 
                # followed the pattern of a boolean chart.
                # e.g. for N = 4, light will be on when states are ON,ON,ON,ON, equivalent to 2^4-1 = 31 snaps.
                # Similar logic was extended to general N.
                
                light = 'OFF'
                
                power = base ** Ndevices
                onvalue = power - 1L                 
                
                neteffect = Ksnaps % power
                
                if neteffect == onvalue:
                    light = 'ON'
                else:
                    light = 'OFF' 
                    
 
                results.append(light)       
            # cases finished
                  
    if DEBUG:
        print results
        
    #output to file
    if len(results) > 0 and fOK :
        fOK = writeToFile(outputFile, results)
    
    return fOK              
# end of module                
            
            
if __name__ == "__main__":
    
    if ASKFORFILE:
        #input file paths
        inputFile = (raw_input('Enter input file path: '))
        outputFile = (raw_input('Enter output file path: '))
    else:
        inputFile = example1_in
        outputFile = example1_out
    
    if DEBUG:
        print inputFile
        print outputFile
    
    # solve the problem    
    fOK = snapper(inputFile, outputFile)
    
    if fOK:    
        print "Successfully completed. Check the file at \r" + outputFile
    else:
        print "Error. Some problem with input file at \r" + inputFile
                