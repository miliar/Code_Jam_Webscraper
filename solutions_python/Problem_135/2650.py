# -*- coding: utf-8 -*-

from os import path


def getDataFile(dataFileName) :
    thisFolderPath = path.dirname( path.abspath( __file__ ) )
    dataFolderPath = path.join(thisFolderPath, "..", 'data')

    return path.join(dataFolderPath, dataFileName)

def getLayout(dataFile) :
    layout = {}
    for i in range(4) :
        line = dataFile.readline().split()
        layout[i + 1] = line
    return layout

########################################
# Main Process Start
########################################
DATA_FILE_NAME = 'A-small-attempt1.in'

with open(getDataFile(DATA_FILE_NAME),'r') as dataFile :
    testCaseNum = int(dataFile.readline())

    for i in range(testCaseNum) :
        firstAnswer = int(dataFile.readline())
        firstLayout = getLayout(dataFile)
        secondAnswer = int(dataFile.readline())
        secondLayout = getLayout(dataFile)

        firstAnswerLineSet = set(firstLayout[firstAnswer])
        secondAnswerLineSet = set(secondLayout[secondAnswer])

        commonSet = firstAnswerLineSet & secondAnswerLineSet

        print 'Case#' + str(i + 1) +": ",

        if len(commonSet) == 1 :
            print commonSet.pop()
        elif len(commonSet) == 0 :
            print "Volunteer cheated!"
        else :
            print "Bad magician!"
