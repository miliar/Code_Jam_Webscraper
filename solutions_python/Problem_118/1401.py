#   CodeJam 2012
#   Nick: geekchimp
#   Description: File Operations

__author__ = 'Ganesh'

def readFile(inputFileName):
    """Takes the file Name as String , And returns a list.
        Element of the list are the data in the corresponding line
        The data in the file should not containg spacing between each line"""
    f = open(inputFileName,"r")

    # data = []
    # while True:
    #     text = f.readline()
    #     text = text.strip()
    #     text = text.strip("\n")
    #     if text == "":
    #         break
    #     data.append(text)
    # f.close()
    # return data
    return stripLineBreak(f.readlines())

def outFile(outputFileName,data):
    """Takes in Output FileName as String and a List whose Element
        contains answers to the corresponding Case
        ELEMENTS OF LIST SHOULD BE STRING"""
    file = open(outputFileName,"w")
    for i in range(len(data)):
        s = "Case #%d: " %(i+1) + str(data[i])+"\n"
        file.write(s)
    file.close()
    return

def stripLineBreak(lines):
    for i in xrange(len(lines)):
        lines[i] = lines[i].strip("\n")
    return lines