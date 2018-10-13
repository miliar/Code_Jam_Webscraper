def getToken(filename):
    inputFile = open(filename, 'r')
    for line in inputFile:
        tokens = line.split()
        for token in tokens:
            if token != '':
                yield token
    inputFile.close()

inputFilename = 'B-small-attempt0.in'
outputFilename = 'B-small-attempt0.txt'

tokenIterator = getToken(inputFilename)
def get():return tokenIterator.next()
def getint(): return int(get())
outputFile = open(outputFilename, 'w')

# END PRE-PROCESSING

caseNum = getint()
for case in range(caseNum):

    transform = {}
    forbid = set()
    
    transformNum = getint()
    for tt in range(transformNum):
        s = get()
        transform[s[:2]] = s[2]
    forbidNum = getint()
    for tt in range(forbidNum):
        s = get()
        forbid.add(s)
    lenNum = getint()
    word = get()

    l = []

    def forbidLetter(letter):
        for x in l:
            if x+letter in forbid or letter+x in forbid:
                return True
        return False

    for letter in word:
        if len(l)>0:
            if l[-1]+letter in transform:
                l[-1] = transform[l[-1]+letter]
            elif letter+l[-1] in transform:
                l[-1] = transform[letter+l[-1]]
            elif forbidLetter(letter):
                l = []
            else:
                l.append(letter)
        else:
            l.append(letter)

    output = "Case #"+str(case+1)+": ["+", ".join(l)+"]"
    outputFile.write(output+"\n")

# BEGIN POST-PROCESSING
outputFile.close()

