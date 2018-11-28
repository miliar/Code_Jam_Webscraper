"""
python solution for magictrick
author: _where
"""
outfile = open('output.out', 'w')
def initial():
    infile = open('input.in')
    testCases = int(infile.readline())
    for p in range(testCases):
        outfile.write('Case #%s: ' % (p+1),)
        initArray = []
        secondArray = []
        initChoice = int(infile.readline()) - 1
        for n in range(4):
            initArray.append([x for x in infile.readline().rstrip().split(' ')])
        secondChoice = int(infile.readline()) - 1
        for n in range(4):
            secondArray.append([x for x in infile.readline().rstrip().split(' ')])
        #analyze(initArray, secondArray, initChoice, secondChoice)
        if (p+1 != testCases): analyze(initArray, secondArray, initChoice, secondChoice, False)
        else: analyze(initArray, secondArray, initChoice, secondChoice, True)
    outfile.close()
    infile.close()

def analyze(initArray, secondArray, initChoice, secondChoice, boo):
    similar = 0
    value = []
    for x in initArray[initChoice]:
        if x in secondArray[secondChoice]:
            similar+=1
            value.append(x)
    if similar == 1:
        outfile.write('%s' % value[0])
        if not boo: outfile.write('\n')
    elif similar == 0:
        outfile.write('Volunteer cheated!')
        if not boo: print outfile.write('\n')
    elif similar > 1:
        outfile.write('Bad magician!')
        if not boo: outfile.write('\n')
if __name__ == '__main__':
    initial();