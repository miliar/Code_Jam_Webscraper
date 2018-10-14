'''
Created on May 7, 2011

@author: doronv
'''
'''
Created on May 7, 2011

@author: doronv
'''

## import section
import re
import filecmp

## folder definitions
## input folder
rootFolder = 'C:/Documents and Settings/Veltzer Doron/My Documents/My Dropbox/Programming/GoogleCodeJam'
inputsFolder = 'inputs'
outputsFolder = 'outputs'
yearFolder = '2011'
stageFolder = 'Qual'
projectLetter = 'D'

example = False
if (example):
    fileName = projectLetter + '-def'
    examplePath = rootFolder + '/' + outputsFolder + '/' + yearFolder + stageFolder + '/' + fileName + '.example'
else:
##    fileName = projectLetter + '-small-attempt1'
    fileName = projectLetter + '-large'

inputPath = rootFolder + '/' + inputsFolder + '/' + yearFolder + stageFolder + '/' + fileName + '.in'
outputPath = rootFolder + '/' + outputsFolder + '/' + yearFolder + stageFolder + '/' + fileName + '.out'


## open input
input = open(inputPath, 'r')
output = open(outputPath, 'w')


## handle input
## read case number
match = re.search('(\d+)', input.readline())
T = int(match.group(1))

## iterate on all cases
for t in range(T):
    ## case input parameter counter 
    match = re.search('(\d+)', input.readline())
    N = int(match.group(1))

    values = input.readline().split(' ')
    
    ## run sort of a shuffle sort (we either count the sum length of all
    ## circular sub lists or even simpler simply count the elements that are not in place,
    ## the sorting will work anyway, just tell Goro to hold the ones in place in each stage
    ## hit the table and then repeat as needed)
    count = 0
    for n in xrange(N):
        if (int(values[n]) != n + 1 ):
            count = count + 1
            continue;


    ## output case result
    outputLine = 'Case #' + str(t + 1)+ ': '  + '%.6f'%(float (count))  + '\n'
    if (example):
        print(outputLine)
    output.write(outputLine)

input.close()
output.close()

## if this is an example run then compare the output to the example output file
if (example):
    if (filecmp.cmp(outputPath, examplePath)):
        print('Def result match OK')
    else:
        print('ERROR: Def result differ')

####print input.read()
##while 1:
####    char = input.read(1)          # read by character
##    line = input.readline()          # read by character
##    if not line: break
##    print line,
