#   Google Code Jam 2015 Qualification
#   
#   A. Standing Ovation
#
#   Author: Yogeshwar M V
#   Email: yog.venkatesh@gmail.com
#   11/04/2015
#
#   Usage: A.py <dataset size>
#   Valid size arguments: small, large

import os, sys

INPUT_FILE_PATH = ""
OUTPUT_FILE_PATH = ""
try:
    if sys.argv[1] == "small":
        INPUT_FILE_PATH = "/Users/Yogi/Desktop/Google Code Jam 2015/Qualification/A-small-attempt0.in.txt"
        OUTPUT_FILE_PATH = "/Users/Yogi/Desktop/Google Code Jam 2015/Qualification/A-small.out.txt"
    elif sys.argv[1] == "large":
        INPUT_FILE_PATH = "/Users/Yogi/Desktop/Google Code Jam 2015/Qualification/A-large.in.txt"
        OUTPUT_FILE_PATH = "/Users/Yogi/Desktop/Google Code Jam 2015/Qualification/A-large.out.txt"
    elif sys.argv[1] == "test":
        INPUT_FILE_PATH = "/Users/Yogi/Desktop/Google Code Jam 2015/Qualification/A-test.in.txt"
        OUTPUT_FILE_PATH = "/Users/Yogi/Desktop/Google Code Jam 2015/Qualification/A-test.out.txt"
    else:
        print "Invalid dataset size!"
        sys.exit()
except IndexError:
    print "\nSpecify dataset size!\n"
    sys.exit()
except:
    print "\nError\n"
    sys.exit()

if os.path.isfile(OUTPUT_FILE_PATH):
    os.remove(OUTPUT_FILE_PATH)

def getInput():
    f = open(INPUT_FILE_PATH, "r")
    ip = f.readlines()
    f.close()
    ip = [line.strip() for line in ip]
    return ip

def writeOutputLine(line):
    f = open(OUTPUT_FILE_PATH, "a")
    f.write(line+"\n")
    f.close()

def writeOutput(output):
    op = [line+"\n" for line in output]
    f = open(OUTPUT_FILE, "w")
    f.writelines(op)
    f.close()

def printOutputLine(output):
    print output


#### Problem specific functions ####

def checkAllAreClapping(audString, additionalClappers):
    allAreClapping = True
    for i in range(0, len(audString)):
        clapping = 0+additionalClappers
        for k in list(reversed(range(0, i))):
            clapping += int(audString[k])
        if clapping < i:
            allAreClapping = False
    
    return allAreClapping
    
####################################
    
inputLines = getInput()

currentLine = 0
cases = int(inputLines[currentLine])
caseCount = 1
currentLine += 1

while currentLine <= cases:
    thisCase = inputLines[currentLine].split()
    sMax = int(thisCase[0])
    aud = thisCase[1]
    
    clappersRequired = 0
    
    for k in range(0, sMax+1):
        while not checkAllAreClapping(aud[:k+1], clappersRequired):
            clappersRequired += 1
        
    opLine = "Case #"+str(caseCount)+": "+str(clappersRequired)
    writeOutputLine(opLine)
    printOutputLine(opLine)
    caseCount += 1
    currentLine += 1

