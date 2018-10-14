import sys
import io

inputFile = sys.argv[1]
outFile = sys.argv[2]


class TidyNumber:
    def __init__(self,file):
        number = file.readline().strip()
        isStartOfNumber=True
        didDecreaseAlready = False
        answer = io.BytesIO()
        isInSameNumberFlush = False
        flushLength = 0
        isStartOfNumberInFlash=False

        # Either I'm writing what I current have
        # Or I can simply right 9s till the end
        length = len(number)
        for currentIndex in xrange(length):
            if(didDecreaseAlready):
                answer.write("9")
            elif(isInSameNumberFlush): #rethink way to do this if?
                if (currentIndex < length - 1):
                    curChar = number[currentIndex]
                    nextChar = number[currentIndex + 1]
                    if (curChar < nextChar):
                        for i in xrange(flushLength):  # reached the end in flush
                            answer.write(number[currentIndex])
                        isInSameNumberFlush=False
                    elif (curChar == nextChar):
                        flushLength += 1
                    else:
                        isInSameNumberFlush = False
                        didDecreaseAlready = True
                        if (isStartOfNumberInFlash and curChar == '1'):
                            for i in xrange(flushLength-1):  # reached the end in flush
                                answer.write('9')
                        else:
                            answer.write(chr(ord(curChar)-1))
                            for i in xrange(flushLength-1):  # reached the end in flush
                                answer.write('9')
                else:
                    for i in xrange(flushLength): # reached the end in flush
                        answer.write(number[currentIndex])
            else:
                if (currentIndex<length-1):
                    curChar = number[currentIndex]
                    nextChar = number[currentIndex+1]
                    if(curChar<nextChar):
                        answer.write(curChar)
                    elif(curChar==nextChar):
                        isInSameNumberFlush=True
                        isStartOfNumberInFlash = isStartOfNumber
                        flushLength=2
                    else:
                        didDecreaseAlready=True
                        if(isStartOfNumber and curChar=='1'):
                            continue #this will be changed to a 0
                        answer.write(chr(ord(curChar)-1))

                else: answer.write(number[currentIndex])
            isStartOfNumber=False

        self.result=answer.getvalue()
        answer.close()



f = open(inputFile,"r")

firstLine = f.readline()
numberOfWords = int(firstLine)
print numberOfWords
o = open(outFile, "w")
i=0
for wordNumber in xrange(numberOfWords):
    i+=1
    d = TidyNumber(f)
    print "Case #{0}: {1}".format(i,d.result)

    o.write( "Case #{0}: {1}\n".format(i,d.result))