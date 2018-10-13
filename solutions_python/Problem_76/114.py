'''
Created on May 7, 2011

@author: doronv
'''

## import section
import re
import filecmp

## folder definitions
## input folder
rootFolder = 'C:/Documents and Settings/Doron Veltzer.DORON/My Documents/My Dropbox/Programming/GoogleCodeJam'
inputsFolder = 'inputs'
outputsFolder = 'outputs'
yearFolder = '2011'
stageFolder = 'Qual'
projectLetter = 'C'

example = False

if (example):
    fileName = projectLetter + '-def'
    examplePath = rootFolder + '/' + outputsFolder + '/' + yearFolder + stageFolder + '/' + fileName + '.example'
else:
##    fileName = projectLetter + '-small-attempt0'
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

    ## read the N candy values
    line = input.readline().split(' ')
    candy = list()
    for n in xrange(N):
        candy.append(int(line[n]))

    ## note: since Patrick is in fact doing a bitwise xor for any given pile subdivision
    ## the two groups will be equal only if their xor is equal which means that the xor
    ## of the entire candy value list is equal to 0, if this is not the case then such
    ## an equal sub-division is not possible, if the overall xor is 0 on the other hand
    ## then Sean can give Patrick as little real value as possible (barring the empty pile)
    ## which will always turn out to be the lowliest candy in the pile
       
    ## first let's rule out the No solution case
    candyXor = 0
    for n in xrange(N):
        candyXor = candyXor ^ candy[n]
    
    if (candyXor != 0):
        result = 'NO'
    else:
        result = str(sum(candy) - min(candy))

    ## output case result
    outputLine = 'Case #' + str(t + 1)+ ': '  + result + '\n'
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