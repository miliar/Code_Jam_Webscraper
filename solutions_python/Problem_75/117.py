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
projectLetter = 'B'

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

    ## read case line and split it to case parameters
    line = input.readline()
    lineSplit = line.split(' ')
    
    ## case input parameter counter 
    counter = 0

    ## read combinations
    C = int(lineSplit[counter])
    counter = counter + 1
    combinations = dict()
    ## read C combinations
    for c in xrange(C):
        combination = lineSplit[counter]
        counter = counter + 1
        
        ## enter both combination orders into the combinations dictionary hash
        combinations[combination[0] + combination[1]] = combination[2]
        combinations[combination[1] + combination[0]] = combination[2]

    ## read combinations
    D = int(lineSplit[counter])
    counter = counter + 1
    oppositions = dict()
    ## read D oppositions
    for d in xrange(D):
        opposition = lineSplit[counter]
        counter = counter + 1

        ## enter both opposition orders into the oppositions dictionary hash
        oppositions[opposition[0] + opposition[1]] = 1
        oppositions[opposition[1] + opposition[0]] = 1


##    print combinations
##    print oppositions
    
    ## read and perform invocations
    N = int(lineSplit[counter])
    counter = counter + 1
    invokations = lineSplit[counter]
    
    ## current element list
    current = list()
    
    ## invoke in order to get the current element list at the end
    for n in xrange(N):##        print current

        
        ## handle combine
        invokation = invokations[n]
##        print invokation
        handled = False
        if (len(current) > 0):
            last = len(current) - 1
            combination = current[last] + invokation
            if (combination in combinations):
                ## combine to generate a non envokable element 
                current[last] = combinations[combination]
                handled = True

        ## handle oppose
        if (not handled): 
            for i in xrange(len(current)):  ## I could handle this better with a graph but this is good enough for just 64 possibilities
                opposition = current[i] + invokation
                if (opposition in oppositions):
                    ## clear the current list
                    current = list()
                    handled = True
                    break;
                        ## otherwise just add the element to the list
        if (not handled): 
            current.append(invokation)

    ## output case result
    outputLine = 'Case #' + str(t + 1)+ ': '  + re.sub('\'', '', str(current)) + '\n'
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