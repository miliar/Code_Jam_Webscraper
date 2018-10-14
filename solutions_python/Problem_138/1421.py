import re
'''
def optimalDeceitfulPlay(NaomiBlocks, KenBlocks, numBlocks):
    count = 0
    for block in NaomiBlocks:
        if block < KenBlocks[0]:
            count += 1
    return numBlocks - count
'''

def optimalWarPlay(NaomiBlocks, KenBlocks, numBlocks):
    count = 0
    for block in NaomiBlocks:
        for i in range(len(KenBlocks)):
            if block < KenBlocks[i]:
                KenBlocks.pop(i)
                count += 1
                break
    return count
                

def DeceitfulWar(inFile):
    f = open('DeceitfulWarOutput.txt', 'w')
    T = int(inFile.readline())
    testCase = 1
    while testCase <= T:
    
        numBlocks = int(inFile.readline())
        NaomiBlocks = re.split(' |\n', inFile.readline())
        NaomiBlocks.pop()
        NaomiBlocks.sort()

        KenBlocks = re.split(' |\n', inFile.readline())
        if testCase != T:
            KenBlocks.pop()
        if testCase == T:
            KenBlocks.pop()
        KenBlocks.sort()
        
        Naomi2 = list(NaomiBlocks)
        Ken2 = list(KenBlocks)

        
        f.write('Case #' + str(testCase) + ': ' + \
                str(optimalWarPlay(KenBlocks, NaomiBlocks, numBlocks)) + \
                ' ' + str(numBlocks - optimalWarPlay(Naomi2, Ken2, numBlocks)) + \
                '\n')
        testCase += 1
