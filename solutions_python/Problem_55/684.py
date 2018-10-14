#!/usr/bin/python
# Filename: themepark.py

'''
Created on May 8, 2010

@author: zeest
'''

'''
NOTES: Files must have \n as separator

'''


'''
Problem Statement: Theme Park

Problem
Roller coasters are so much fun! It seems like everybody who visits the theme park wants to ride the roller coaster. Some people go alone; other people go in groups, and don't want to board the roller coaster unless they can all go together. And everyone who rides the roller coaster wants to ride again. A ride costs 1 Euro per person; your job is to figure out how much money the roller coaster will make today.
The roller coaster can hold k people at once. People queue for it in groups. Groups board the roller coaster, one at a time, until there are no more groups left or there is no room for the next group; then the roller coaster goes, whether it's full or not. Once the ride is over, all of its passengers re-queue in the same order. The roller coaster will run R times in a day.
For example, suppose R=4, k=6, and there are four groups of people with sizes: 1, 4, 2, 1. The first time the roller coaster goes, the first two groups [1, 4] will ride, leaving an empty seat (the group of 2 won't fit, and the group of 1 can't go ahead of them). Then they'll go to the back of the queue, which now looks like 2, 1, 1, 4. The second time, the coaster will hold 4 people: [2, 1, 1]. Now the queue looks like 4, 2, 1, 1. The third time, it will hold 6 people: [4, 2]. Now the queue looks like [1, 1, 4, 2]. Finally, it will hold 6 people: [1, 1, 4]. The roller coaster has made a total of 21 Euros!
Input
The first line of the input gives the number of test cases, T. T test cases follow, with each test case consisting of two lines. The first line contains three space-separated integers: R, k and N. The second line contains N space-separated integers gi, each of which is the size of a group that wants to ride. g0 is the size of the first group, g1 is the size of the second group, etc.
Output
For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of Euros made by the roller coaster.
Limits
1 <= T <= 50.
g[i] <= k.

Small dataset
1 <= R <= 1000.
1 <= k <= 100.
1 <= N <= 10.
1 <= g[i] <= 10.

Large dataset
1 <= R <= 108.
1 <= k <= 109.
1 <= N <= 1000.
1 <= g[i] <= 107.
Sample

Input 
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3 


Output 
Case #1: 21
Case #2: 100
Case #3: 20



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

def themepark (inputFile, outputFile):    
    ''' Solves Theme Park example.
    
    Elegantly '''
   
    fOK = True
    
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
                tS = 1+t*2
                Rrounds = long(data [tS][0])
                kSize = long(data [tS][1])
                Ngroups = long(data [tS][2])
                
                tD = 2+t*2
                groups = data[tD]
                
                if DEBUG:
                    print 'Groups: ' + str(Ngroups) + '\tRounds: ' + str(Rrounds) + '\tSize: ' + str(kSize)
                    print groups
                    
                # begin working on the round
                euros = 0
                queue = groups
                
                for round in range(0, Rrounds):
                    oncoaster = []
                    onride = 0
                    
                    #start moving people to coaster
                    for g in range (0, Ngroups):
                        # pop from list
                        persons = queue[0]
                        more = long(persons)
                        
                        if (onride + more) <= kSize:
                            onride = onride + more
                            del queue[0] # remove from list
                            oncoaster.append(persons) # on the coaster     
                        else:
                            break
                        
                        if DEBUG:
                            print 'Queue Size: ' + str(len(queue)) + '   Queue: '+ str(queue)
                            print 'Persons on the ride: ' + str(onride)
                    # groups finished  
                # rounds finished
                            
                    euros = euros + onride
                    queue.extend(oncoaster) # people back to queue 
                    
                results.append(str(euros))       
            # cases finished
                  
    if DEBUG:
        print results
        
    #output to file
    if len(results) > 0 and fOK :
        fOK = writeToFile(outputFile, results)
    
    if fOK:    
        print "Successfully completed. Check the file at \r" + outputFile
    else:
        print "Error. Some problem with input file at \r" + inputFile    
        
                    
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
    themepark(inputFile, outputFile)
                