import sys, os, csv
import logging


#############################################################################
class Snapper(object) :
    def __init__ (self, fileName) :
        self.noOfTestCases = 0
        self.data = dict();

        self.readData(fileName)

        #print self.data[0]
        self.logger = logging.getLogger("Snapper")

        self.result = dict()

        self.output = open(fileName.replace(".in", "") + ".out", 'w')

    def readData(self, fileName) :
        testCaseNo = 0
        try :
            fileIn = open(fileName, 'r');
            firstLine = True
            oddLine = True
            noofmarbels = 0
            for line in fileIn:
                if firstLine :
                    firstLine = False
                    self.noOfTestCases = int(line.strip())
                    continue

                else :
                    strings = line.strip().split(' ')
                    #print strings
                    self.data[testCaseNo] = (int(strings[0]), int(strings[1]))
                    testCaseNo += 1
                        
        except :
            print "invalid data set"

        assert self.noOfTestCases == testCaseNo
        #print self.data



    def printResult(self) :
        for index in range(1, self.noOfTestCases + 1) :
            print "Case #%d: %s" % ( index, str(self.result[index])) 
            print >> self.output, "Case #%d: %s" % ( index, str(self.result[index])) 

    def runTestCases(self) :
        for index in range(self.noOfTestCases) :
            self.runOneTestCase(index);
                    
    def createSnapperList(self, noOfSnaps) :
        list1 = []
        for index in range (noOfSnaps) :
            list1.append(False) 
        
        return list1
        
    def switchOn(self, index, noOfSnapper, snapperList) :

        if index >= noOfSnapper :
            return
    
        if snapperList[index] == True :
            nextNext = index + 1
            self.switchOn(nextNext, noOfSnapper, snapperList)
            
            snapperList[index] = False
        else :
            snapperList[index] = True

    def runOneTestCase(self, index) :

        noOfSnapper, noOfSnap = self.data[index]
        snapperList = self.createSnapperList(noOfSnapper)
        while (noOfSnap) :
            noOfSnap -= 1
            self.switchOn(0, noOfSnapper, snapperList)
        

        on = True
        for elem in snapperList :
            if elem == False :
                on = False
                break
        if on == True :
            self.result[index + 1] = "ON"
        else :
            self.result[index + 1] = "OFF"


    
#############################################################################
if __name__ == "__main__" :
    logging.basicConfig(level = logging.DEBUG,
                format= '%(levelname)-8s %(message)s', 
                filename = "snapper.log",
                filemode='w')
    logger = logging.getLogger("Snapper")
    console = logging.StreamHandler()
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    console.setLevel(logging.DEBUG)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    if len(sys.argv) != 2 :
        logger.error("Invalid no of parameters are passed.")
        logger.error("Usage : python snapper.py <test.txt>.")
        exit(1);
        

    file = sys.argv[1]
    #logger.info("test case to be tested : " + file)
    if not os.path.isfile(file) :
        logger.info(file + " : file doesn't exist.")

    snapper = Snapper(file)
    snapper.runTestCases()
    snapper.printResult()
