from sys import stdin

def main():
    firstline = stdin.readline().split()
    length = int(firstline[0])
    numberOfWords = int(firstline[1])
    testCases = int(firstline[2])
    
    words = []
    testWords = []

    for i in xrange(0,numberOfWords):
        words.append(stdin.readline().strip())
    for i in xrange(0,testCases):
        testWords.append(stdin.readline().strip())

    case = 0
    for testWord in testWords:
        wordlist = makeWordList(testWord)
        case += 1
        count = 0

        for word in words:
            for i in range(len(wordlist)):
                if word[i] in wordlist[i]:
                    if i+1 == len(wordlist):
                        count += 1
                else:
                    break
        print "Case #%s: %s" % (case, count)

    for testWord in testWords:
        wordlist

def makeWordList(string):
    wordList = []
    word = ""

    multiple = False
    
    for letter in string:
        if letter == '(':
            word == ""
            multiple = True
            continue
        elif letter == ')':
            wordList.append(word)
            multiple = False
            word = ""
            continue

        if multiple:
            word += letter
            continue
        else:
            wordList.append(letter)
    return wordList

main()
