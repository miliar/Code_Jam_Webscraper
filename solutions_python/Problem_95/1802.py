filesDir = '/home/alberto/py/'
inFile = 'A-small-attempt0.in'

def writeToFile(filename,content):
    f = open(filesDir + filename,'w')
    f.write(content)
    f.close()

def readFileLines(filename):
    f = open(filesDir + filename,'r')
    t = f.readlines()
    t.pop(0)
    g = []
    for l in t:
        g.append(l.replace('\n',''))
    return g

def processArray(array):
    output = ''
    curCase = 1
    for line in array:
        curLine = 'Case #' + str(curCase) + ': ' + processLine(line) + '\n'
        output += curLine
        curCase += 1
    return output

def procedure():
    outFile = inFile.replace('.in','.out')
    array = readFileLines(inFile)
    processedArray = processArray(array)
    writeToFile(outFile,processedArray)

charmap = {'a':'y',
           'b':'n',
           'c':'f',
           'd':'i',
           'e':'c',
           'f':'w',
           'g':'l',
           'h':'b',
           'i':'k',
           'j':'u',
           'k':'o',
           'l':'m',
           'm':'x',
           'n':'s',
           'o':'e',
           'p':'v',
           'q':'z',
           'r':'p',
           's':'d',
           't':'r',
           'u':'j',
           'v':'g',
           'w':'t',
           'x':'h',
           'y':'a',
           'z':'q'
           }

def replace_all(input):
    for i,j in charmap.iteritems():
        input = input.replace(j,i.upper())
    return input.lower()

def processLine(input):
    output = replace_all(input)
    return output

procedure()


