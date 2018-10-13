import csv
import collections
import threading

def threadSafe(function):
    """Decorator to lock possible thread unsafe stuff"""
    theLock = threading.Lock() #Create a lock in this functions namespace
    def wrapper(*args,**kwargs):
        with theLock:
            return function(*args,**kwargs)

    return wrapper

class ThreadDispatcher(threading.Thread):
    """Nice Simple Class to Setup and Run Tasks"""
    def __init__(self,fileHandler):
        """
        Create A dispatcher
        @param fileHandler: Link to object that serves data
        """
        threading.Thread.__init__(self)
        self.fileHandler = fileHandler
        

    def run(self):
        """Generallised Running"""
        while True:
        #for x in range(10):
            case,data = self.fileHandler.next()
#            print case
            if not case:
                break
            else:
                output = self.runMethod(data)
            self.fileHandler.appendOut(case,output)

    def runMethod(self,data):
        """Overload this"""
        
        #time.sleep(float(data[0]))
        #print data
        return data

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
        """Quick and dirty output Script,
        Append to the correct test case position"""
        self.outArr[index-1] = (index,value)

    @threadSafe
    def writeOut(self,fileName):
        print self.outArr
        with open(fileName,"w") as fd:
            for item in self.outArr:
                fd.write("Case #%s: %s\n" %(item[0],item[1]))
    @threadSafe
    def next(self):
        """Return the next test case
        @param return: Test Index,(Test Data)
        """
        fileReader = self.reader
        #params = self._getNext()
        try:
            params = self._getNext()
        except StopIteration:
            return None,None

        idx = self.testIndex#
        self.testIndex += 1
        return idx,params

    def _getNext(self):
        """Overload Accoring to Input"""
        fileReader = self.reader
        params = fileReader.next()
        return params

#self.corDict.sort(key=lambda x:x[0])

class dispatch(ThreadDispatcher):
    def runMethod(self,data):
        print "==="
        num,wires =  data
        print wires
        print "---"
        #print wires
        cross = 0
        for idx in range(num):
            thisWire = wires[idx]
            inIdx = idx + 1
            print thisWire
            while inIdx < num:
                nextWire = wires[inIdx]
                if thisWire[0] < nextWire[0]:
                    if thisWire[1] > nextWire[1]:
                        cross += 1
                else:
                    if thisWire[1] < nextWire[1]:
                        cross += 1
                inIdx += 1

        print "=>> ",cross
        return cross
                

class myReader(fileReader):
    def _getNext(self):
        """If more than one line per input Overload to make work"""
        #params = [int(x) for x in self.reader.next()]
        rows = self.reader.next()
        rows  = int(rows[0])
        lines = []
        for x in range(rows):
            lines.append([int(x) for x in self.reader.next()])

        lines.sort(key=lambda x:x[0])
        return rows,lines


if __name__ == "__main__":
    import time
    stTime = time.time()
    #reader = myReader("A-small-attempt1.in")
    reader = myReader("A-large.in")
    #reader = myReader("test.in")

    doo = dispatch(reader)
    #reader.next()


#    reader = FileUtils.fileReader()
    #reader = myReader("C-large-practice.in")

    dispatcher = [dispatch(reader) for x in range(1)]
    for x in dispatcher:
        x.start()
        
    for x in dispatcher:
        x.join()
        
    reader.writeOut("largeOut.dat")    
    
    edTime = time.time()
    print "Start\t%s "%time.ctime(stTime)
    print "End\t%s "%time.ctime(edTime)
    print "Total\t%s" %(edTime-stTime)


