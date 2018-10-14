from PermutationFinder import PermutationFinder

def getSearchableSequence(dictionary, word, maxWordLength):
    pf = PermutationFinder(word, maxWordLength, dictionary)
    word = pf.findPermutation()
    return word

def init():
    filename="d:/A-small-attempt0.in"
    contents=readContents(filename)
    numbers,dictionary,encodedSequence=getData(contents)
    word=encodedSequence[0]
    maxWordLength=int(numbers[0])
    i=1
    result=""
    for word in encodedSequence:
        sequencedWord = getSearchableSequence(dictionary, word, maxWordLength)
        possibleInterpretation=getMaxInterpretation(sequencedWord,dictionary)
        result+="Case #"+str(i)+": "+str(possibleInterpretation)+"\n"
        i+=1
    print result

def getMaxInterpretation(word,dictionary):
    maxInterpretation=0
    for entry in dictionary:
        if len(word)==len(entry):
            exists=1
            for i in range(len(entry)):
                try:
                    ok=word[i].index(entry[i])>=0
                except ValueError:
                    exists=0
                    break
            if exists==1:
                maxInterpretation+=1
    return maxInterpretation  

def readContents(filename):
    fl=open(filename)
    content=fl.read()
    return content

def getData(content):
    numbers=[]
    words=[]
    encodedSequence=[]
    lines=content.split("\n")
    numbers=lines[0].split(" ")
    for i in range(1,int(numbers[1])+1):
        words.append(list(lines[i]))
    for i in range(int(numbers[1])+1,int(numbers[1])+int(numbers[2])+1):
        encodedSequence.append(lines[i])
    return numbers,words,encodedSequence

init()

    