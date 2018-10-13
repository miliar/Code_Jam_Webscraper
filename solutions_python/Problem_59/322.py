import csv
import collections
import threading

def threadSafe(function):
    theLock = threading.Lock() #Create a lock in this functions namespace
    def wrapper(*args,**kwargs):
        with theLock:
            return function(*args,**kwargs)

    return wrapper

class fileReader(object):
    """ Generic Class to get all the info we need from the file """
    def __init__(self,fileName):
        """Initialise everything"""
        self.reader = reader  = csv.reader(open(fileName),delimiter=" ")
        #Get lines
        self.totLines = lines = int(reader.next()[0])
        self.testIndex = 1
        self.outArr = [None] * self.totLines

    @threadSafe
    def appendOut(self,index,value):
        """Quick and dirty output Script"""
#        print index,value
        self.outArr[index-1] = (index,value)


    @threadSafe
    def writeOut(self,fileName):
        with open(fileName,"w") as fd:
            for item in self.outArr:
                fd.write("Case #%s: %s\n" %(item[0],item[1]))
#            for idx in range(len(self.outArr)):
#                fd.write("Case #%s: %s\n" %(idx+1,self.outArr[idx]))
                
                        
    @threadSafe
    def nextCase(self):
        """Return the next test case
        @param return: Test Index,(Test Data)
        """
        fileReader = self.reader
        params = fileReader.next()
        params.append(fileReader.next())
        idx = self.testIndex
        self.testIndex += 1
        return idx,params

    @threadSafe
    def nextCaseSafe(self):
        """ Slightly Saner version of next case with some error checking """
        fileReader = self.reader
        idx = self.testIndex
        if idx == self.totLines:
            #print "End Of Cases"
            return idx,None
        
        self.testIndex += 1
        
        params = fileReader.next()
        #params.append(fileReader.next())

        return idx,params

    @threadSafe
    #def nextCaseCatch(self):
    def next(self):
        """Return the next test case
        @param return: Test Index,(Test Data)
        """
        fileReader = self.reader
        try:
            params = self._getNext()
            #params.append(fileReader.next())
        except Exception, e:
            print e
            
            return None,None

        idx = self.testIndex#
        print "Case ",idx
        self.testIndex += 1
        return idx,params

    def _getNext(self):
        """Overload to make work"""
        fileReader = self.reader
        params = fileReader.next()
        return params

FNM = "C-large.in"
#FNM = "C-small-attempt0.in"

# def runTest(): #(CASE 1)
#     testInstance = fileReader(FNM)
#     for x in range(100): #CASE2 Switch to 50
#         testInstance.nextCase()

def runTest():
    testInstance = fileReader(FNM)
    while True:
        try:
            testInstance.nextCase()
        except:
            break

def runTestSafe():
    testInstance = fileReader(FNM)
    while True:
        out = testInstance.nextCaseSafe()
        if not out[0]:
            break

def runTestCatch():
    testInstance = fileReader(FNM)
        
    while True:
        out = testInstance.nextCaseCatch()
        if not out[0]:
            break
        
if __name__ == "__main__":
    import timeit
     
    print "Test"
    t = timeit.Timer("runTest()","from __main__ import runTest")
    print t.repeat(3,500)

    print "Safe"
    t = timeit.Timer("runTestSafe()","from __main__ import runTestSafe")
    print t.repeat(3,500)

    print "Catch"
    t = timeit.Timer("runTestCatch()","from __main__ import runTestCatch")
    print t.repeat(3,500)

    print "Done"


""" Test Results
Case 1: Try to fetch 100 Objects

Normal: Fail
Safe
[0.077474117279052734, 0.077402830123901367, 0.07726287841796875]
Catch
[0.11783695220947266, 0.11929607391357422, 0.11930084228515625]

Case 2: Only fetch the 50 we need
Test
[0.065707921981811523, 0.063865184783935547, 0.063968896865844727]
Safe
[0.067720890045166016, 0.067888021469116211, 0.067918062210083008]
Catch
[0.066517114639282227, 0.066443920135498047, 0.066563129425048828]
Done

Case3 : (While,  No1 Fails, so wrap in try)
Test
[0.065824985504150391, 0.066252946853637695, 0.065771818161010742]
Safe
[0.0097920894622802734, 0.0097699165344238281, 0.0097742080688476562]
Catch
[0.0098769664764404297, 0.0097768306732177734, 0.0097470283508300781]
Done

Case 4: Wrap in Magic Thread Safety

Test
[0.10160493850708008, 0.099607944488525391, 0.099606037139892578]
Safe
[0.010693073272705078, 0.010747909545898438, 0.010756969451904297]
Catch
[0.010525941848754883, 0.010682821273803711, 0.010645866394042969]
Done


Case 5: Large File 
Test
[1.4401350021362305, 1.4227519035339355, 1.422666072845459]
Safe
[0.01134181022644043, 0.011270046234130859, 0.011265039443969727]
Catch
[0.011137008666992188, 0.011248111724853516, 0.011234045028686523]
Done

"""




