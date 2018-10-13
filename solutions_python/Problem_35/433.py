import sys
import string
import os
import array

def LabelBasins(altitudes, height, width):
    labelMap = [[0 for j in range(width)] for i in range(height)]
    nextLabel = 1
    labelDictionary = {}
    for i in range(height):
        for j in range(width):
            mylabel = labelMap[i][j]
            altitude = altitudes[i][j]
            minAltitude = altitude
            direction = -1
            flowi = 0
            flowj  = 0
            #direction = north, west, east, south
            if (i > 0):
                nextAltitude = altitudes[i-1][j]
                if (nextAltitude < minAltitude):
                    flowi = i-1
                    flowj = j
                    minAltitude = nextAltitude
            if (j > 0):
                nextAltitude = altitudes[i][j-1]
                if (nextAltitude < minAltitude):
                    flowi = i
                    flowj = j-1
                    minAltitude = nextAltitude
            if (j < width - 1):
                nextAltitude = altitudes[i][j+1]
                if (nextAltitude < minAltitude):
                    flowi = i
                    flowj = j+1
                    minAltitude = nextAltitude
            if (i < height - 1):
                nextAltitude = altitudes[i+1][j]
                if (nextAltitude < minAltitude):
                    flowi = i+1
                    flowj = j
                    minAltitude = nextAltitude
            #now process the results
            if (minAltitude == altitude):
                #then I am a sink
                if (mylabel == 0):
                    #only do something if I have no label
                    label = nextLabel
                    nextLabel += 1
                    labelDictionary[label] = set([label])
                    labelMap[i][j] = label
            else:
                #I am not a sink, I flow to something
                label = labelMap[flowi][flowj]
                if (label == 0):
                    if (mylabel == 0):
                        #no labels
                        label = nextLabel
                        nextLabel +=1
                        labelDictionary[label] = set([label])
                        labelMap[i][j] = label
                        labelMap[flowi][flowj] = label
                    else:
                        #my label exists
                        labelMap[flowi][flowj] = mylabel
                else:
                    #my sink has a label
                    if (mylabel == 0):
                        labelMap[i][j] = label
                    else:
                        #we both have labels
                        if (mylabel != label):
                            topSet = labelDictionary[mylabel]
                            bottomSet = labelDictionary[label]
                            topSet.update(bottomSet)
                            for crappylabel in topSet:
                                labelDictionary[crappylabel] = topSet
            
                        
    #now everything has a label, all equivalencies are in the dictionary
    #make a label to new label explainer
    #print "old label map"
    #print labelMap
    #print "old label dictionary"
    #print labelDictionary
    newNextLabel = 1
    oldLabelToNewLabelList = [0 for i in range(nextLabel)]
    for label in range(1, nextLabel):
        if (oldLabelToNewLabelList[label] == 0):
            mySet = labelDictionary[label]
            mynewlabel = newNextLabel
            newNextLabel += 1
            for oldequivalentlabel in mySet:
                oldLabelToNewLabelList[oldequivalentlabel] = mynewlabel

    #print oldLabelToNewLabelList
    #We will relabel the labelMap based on the dictionary.
    for i in range(height):
        for j in range(width):
            myoldlabel = labelMap[i][j]
            labelMap[i][j] = oldLabelToNewLabelList[myoldlabel]

    return labelMap
    


#get input info
inputFilename = raw_input("Enter input file name:")
outputFilename = raw_input("Enter output file name:")

inputFile = open(inputFilename)
outputFile = open(outputFilename, 'w')
numMaps = int(inputFile.readline())

labels = "0abcdefghijklmnopqrstuvwxyz"
mapNumber = 0
for mapNumber in range(0, numMaps):        
    infoParts = inputFile.readline().split()
    height = int(infoParts[0])
    width = int(infoParts[1])
    altitudes = [[0 for j in range(width)] for i in range(height)]
    #read in altitudes
    for i in range(height):
        line = inputFile.readline().split()
        for j in range(width):
            altitudes[i][j] = int(line[j])
    if (True):
        print mapNumber
        #print altitudes

        labelMap = LabelBasins(altitudes, height, width)
        #print labelMap
                      
        #Print output      
        outputString = "Case #" + str(mapNumber+1) + ":\n"
        for i in range(height):
            for j in range(width):
                outputString += labels[labelMap[i][j]] + " "
            outputString += "\n"
        outputFile.write(outputString)

inputFile.close()
outputFile.close()
print "done"
