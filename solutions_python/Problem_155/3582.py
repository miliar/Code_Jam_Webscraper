'''
Created on 11-Apr-2015

@author: varunm
'''
def fileRead():
    fo = open("input.txt", "rw+")
    #print "Name of the file: ", fo.name
    lineList = fo.readlines()
    noTestCases = int(lineList[0])
    #print "Total Test Cases : ",noTestCases
#  Enable this for testing all cases    
    for i in range(1, noTestCases+1):
        caseString =  lineList[i]
        splitString(i,caseString)
#    print "Read Line: %s" % (lineList)
    
def splitString(caseId,caseString):
    caseStringSplit = caseString.split( )
    maxShyness =  int(caseStringSplit[0])
    audienceString = caseStringSplit[1]
    solveCase(caseId,maxShyness, audienceString) 
    
def solveCase(caseId,maxShyness, audienceString):
    #print "Max Shyness : ",maxShyness
    #print "Audience String : ", audienceString    
    priorCount = 0
    peopleNeeded = 0
    #iterate over audienceString, check if existing people (prior summation) is >= current shyness, if not, find the difference, and add
    for currentShyness  in range(len(audienceString)):
        audienceCount = int(audienceString[currentShyness])
        #print "Number of audiences with shyness : ",currentShyness, " Are :",audienceCount, "And Prior Count : ",priorCount
        if(audienceCount>0):            
            if(priorCount <= currentShyness):
                peopleNeeded += currentShyness - priorCount
                #print "People Needed : ", peopleNeeded
            priorCount += audienceCount + peopleNeeded
    fo = open("output.txt", "a")
    fo.write("Case #%d: %d\n" %(caseId,peopleNeeded))
    print "Case #%d: %d" %(caseId,peopleNeeded)
    
def main():
    fileRead()
    
if __name__ == "__main__":
    main()
    
    