import linecache

def substrConsonants(string, substrLen):
    j=1
    #listConsonantSubstr=set()
    listConsonantSubstr=[]
    consonants = 'aeiou'
    while True:
        for i in range(len(string)-j+1):
            if len(string[i:i+j]) == substrLen:
                if not any((consonant in string[i:i+j]) for consonant in consonants):
                    listConsonantSubstr.append(string[i:i+j])
        if j==len(string):
            break
        j+=1
    return listConsonantSubstr

def substr(string,listConsonantSubstr):
    j=1
    occurences = 0
    listCombinations=[]
    while True:
        for i in range(len(string)-j+1):
            if any(substring in string[i:i+j] for substring in listConsonantSubstr):
                #listCombinations.append(string[i:i+j])
                occurences += 1
        if j==len(string):
            break
        j+=1
        #string=string[1:]
    return occurences

inputFile = 'A-small-attempt0.in'
testcasesno = int(linecache.getline(inputFile, 1)) + 2
lineNo=1
j = 1

for i in range(2, testcasesno):
    line = ((linecache.getline(inputFile, i).split()))
    print"Case #%d: %d" % (j, substr(line[0],substrConsonants(line[0],int(line[1]))))
    j += 1