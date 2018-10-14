#!/usr/bin/env python



###############################################################################
##  *****     *****    Initial constants    *****     *****
###############################################################################
globals()["PROP_CONFIG_FILENAME"] = "propertyConfigFile"
globals()["PACKAGE_NAME"] = 'image_adaptor'



###############################################################################
##  *****     *****    External modules to import    *****     *****
###############################################################################
# ****   Standard Python Utility Modules
#==============================================================================
import os
import sys

import string



###############################################################################
##  *****     *****    PROCESSING FUNCTIONS     *****     *****
###############################################################################

def loadTests(file_name):
    f = open(file_name, 'r')

    f.readline()
    testLines = f.readlines()

    f.close()


    tests=[]
    for i in testLines:
        tests.append(i.split(' '))
        tests[-1][-1] = tests[-1][-1][:-1]

    return tests

def saveRes(file_name, results):

    f = open(file_name, 'w')

    for i in range(1, len(results)+1):
        f.write("Case #" + str(i) + ": " + str(results[i-1]) + "\r\n")

    f.close()

    return True




###############################################################################
##  *****     *****    MAIN FUNCTION OF THE CODE     *****     *****
###############################################################################


def mainFunction(inputFile):
    tests = loadTests(inputFile)

    results = []

    for i in tests:
        S = int(i[1])
        p = int(i[2])
        points = i[3:]
        print S, "surprises with p=", p, "among the next punctuations:"
        print points

        resSum = 0
        lowLim = p*3-4
        highLim = p*3-3

        print "Limits are:", lowLim, "-", highLim

        for j in points:
            if int(j) > highLim:
                resSum+=1
            elif int(j) == lowLim or int(j) == highLim:
                if S > 0 and int(j) > 1: ## greater than 1 or it can't be surprising!! :O
                    S-=1
                    resSum+=1

        results.append(resSum)
        print "The result is:", resSum

    saveRes(inputFile + ".out", results)
    return 0





###############################################################################
##  *****    *****    ENTRY POINT FOR STARTING THE CODE    *****    *****
###############################################################################

if __name__ == '__main__':
    try:
        inFile = "PrBTest.in"
        if len(sys.argv) > 1:
            inFile = sys.argv[1]
#        else:
#            print "At least the filename is needed!"
        endValue = mainFunction(inFile)
    except Exception as e:
        print "WHOLE-SCOPE EXCEPTION - NODE SHUTTING DOWN"
        print ("Error: %s."%e).center(80, '*')

