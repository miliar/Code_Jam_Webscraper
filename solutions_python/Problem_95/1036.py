filename = "input1.txt"
textFile = open(filename,"r")
theDict = {'z':'q','q':'z',' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
numOfLine = int(textFile.readline()[:-1])

def findDict(string1,string2):
    for i in range(len(string1)):
        theDict[string1[i]] = string2[i]
    return

def giveOutput(string1):
    output = []
    for i in range(len(string1)):
        output.append(theDict[string1[i]])
    output = ''.join(output)
    return output

for i in range(numOfLine):
    string1 = textFile.readline()
    string1 = string1.replace('\n','')
    output = giveOutput(string1)
    print "Case #"+str(i+1)+":  "+output
    

    
