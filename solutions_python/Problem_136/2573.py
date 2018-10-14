# -*- coding: utf-8 -*-

from decimal import Decimal, ROUND_HALF_UP
from os import path
import sys
import time


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
startTime = time.clock()

DATA_FILE_NAME = 'input.txt'

with open(getDataFile(DATA_FILE_NAME),'r') as dataFile :
    testCaseNum = int(dataFile.readline())

    for i in range(testCaseNum) :
        (farmCost, farmProduce, goal) = map(lambda x:Decimal(x), dataFile.readline().split())

        print 'Case #' + str(i + 1) +": ",

        finish = False
        produceCookie = Decimal(2)
        boughtFarmTime = Decimal(0)
        beforeGoaledTime = Decimal(sys.maxint)
        while not finish :
            goaledTime = boughtFarmTime + goal / produceCookie

            if beforeGoaledTime < goaledTime :
                finish = True
            else :
                boughtFarmTime += farmCost / produceCookie
                produceCookie += farmProduce
                beforeGoaledTime = goaledTime

        print beforeGoaledTime.quantize(Decimal('.0000000'), rounding=ROUND_HALF_UP)

    endTime = time.clock()
    print "実行時間： " + str(endTime - startTime) + "秒"
