import sys

if __name__ == "__main__":
    strInputFile = "input.txt"
    strOutputFile = "output.txt"

    try:
        inputFile = open(strInputFile, "r")
        N = int(inputFile.readline())
    except:
        print "Error with file reading : Reading TC count failed"
        sys.exit()
    
    try:
        outputFile = open(strOutputFile, "w")
    except:
        print "Error with file writing : File creation failed"
        sys.exit()
        
    i = 1
    while i <= N:
        #read the test case
        try:
            vectorSize = int(inputFile.readline())
            vector1 = inputFile.readline().rstrip()
            vector2 = inputFile.readline().rstrip()
        except:
            print "Error with file reading: Unable to read vector size & content"
            sys.exit()

        vector1 = vector1.split(" ")
        vector2 = vector2.split(" ")

        vector1 = [int(elt) for elt in vector1]
        vector2 = [int(elt) for elt in vector2]
        
        vector1.sort()
        vector2.sort()
        vector2.reverse()
        
        scalar = 0
        j=0
        while j < vectorSize:
            scalar += vector1[j] * vector2[j]
            j += 1
                
        try:
            outputFile.write("Case #%d: %d\n"%(i, scalar))
        except:
            print "Error with file writing : result not written"
            sys.exit()
                    
        i += 1
        
