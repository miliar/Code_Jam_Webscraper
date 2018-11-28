'''
Author: emmhaych
File Location: /home/emmhaych/Dev/CodeJam/2015/Qualification/D/src/main.py
For license information please refer to LICENSE.txt in the root folder of this project
'''

''' Input/output file names '''
#fileName = 'test'                 # Test input file
#fileName = 'D-small-attempt0'            # Small input file
fileName = 'D-small-attempt1'            # Small input file
#fileName = 'D-large-0'            # Large input file

''' Program start location '''
def main():
    # Open input and output files
    inputFile = open('../inputFiles/' + fileName + '.in', 'r')
    outputFile = open('../outputFiles/' + fileName + '.out', 'w+')
    
    numberOfTestCases = int(inputFile.readline())
    for currentTestCase in range(numberOfTestCases):
        [X, R, C] = list(map(int,inputFile.readline().split()))
        winner = 'RICHARD'
        '''For one omino'''
        # Area % 1 = 0 --> GABRIEL
        if(X == 1):
            winner = 'GABRIEL'
        
        '''For two omino'''
        # Area % 2 = 0 --> GABRIEL
        if(X == 2) and (((R * C) % 2) == 0):
            winner = 'GABRIEL'
        
        '''For three omino'''
        # Area % 3 = 0 --> GABRIEL
        # R and C >= 2 --> GABRIEL
        if(X == 3) and (((R * C) % 3) == 0) and ((R >= 2) and (C >= 2)):
            winner = 'GABRIEL'
        
        ''' For four omino'''
        # Area % 4 = 0 --> GABRIEL
        # R and C >= 3  --> GABRIEL
        if(X == 4) and (((R * C) % 4) == 0) and ((R >= 3) and (C >= 3)):
            winner = 'GABRIEL'
        
        outputFile.write('Case #' + str(currentTestCase + 1) + ': ' + winner + '\n')

if __name__ == '__main__':
    main()