__author__ = 'Gantmajer'

''' I'm using the numpy library. http://www.numpy.org/ '''
from numpy import array, mean, round

fail = 'Fegla Won'

if __name__ == '__main__':
    inFile = open('A-small-attempt0.in', 'r')
    numberOfTests = int(inFile.readline())
    outFile = open('A-small-attempt0.out', 'w')
    for i in range(1, numberOfTests + 1):
        nString = int(inFile.readline())
        oldLetters = []
        nLetters = []
        result = ''
        for j in range(nString):
            newLetters = []
            numberL = []
            word = inFile.readline()
            while(word != '\n'):
                newLetters.append(word[0])
                li = len(word)
                word = word.lstrip(word[0])
                numberL.append(li - len(word))
            if oldLetters and oldLetters != newLetters:
                result = fail
            oldLetters = newLetters[:]
            nLetters.append(numberL)
        if result != fail:
            nLetters = array(nLetters)
            print
            nLetMean = round(mean(nLetters, axis = 0))
            dif = abs(nLetters - nLetMean)
            result = int(sum(sum(dif)))
        outFile.write('Case #%d: %s\n' % (i, result))