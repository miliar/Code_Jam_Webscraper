'''def countWords(case, graph):
    numberWords = 0
    position = graph
    for index, char in enumerate(case):
        try:
            position = position[char]
        except KeyError:
            #This word doesn't exist
            return 0
        if position == {}:
            numberWords += 1
            position = graph
    return numberWords'''

def formCases(case, graph):
    global casesDone

    numberWords = 0
    inParenthesis = False
    parenthesisPos = 0
    possibleStack = []
    position = graph
    
    '''if not '(' in case and not ')' in case:
        numberWords += countWords(case, graph)
        return numberWords'''

    for index, char in enumerate(case):
        if inParenthesis and char == ')':
            inParenthesis = False
            while len(possibleStack) > 0:
                nextCase = '%s%s%s' % (case[:parenthesisPos], possibleStack.pop(0), case[index+1:])
                numberWords += formCases(nextCase, graph)
            break
        elif inParenthesis:
            possibleStack.append(char)
            continue
        if char == '(':
            parenthesisPos = index
            inParenthesis = True
            continue
        try:
            position = position[char]
        except KeyError:
            #This word doesn't exist
            break
        if position == {}:
            numberWords += 1
            position = graph

    return numberWords

file = open('inputAlien', 'r')
lengthOfWord, numberOfWords, numberOfTestcases = [int(x) for x in file.readline().rstrip().split(' ')]
words = [file.readline().rstrip() for x in xrange(numberOfWords)]
testCases = [file.readline().rstrip() for x in xrange(numberOfTestcases)]
file.close()

graph = {}
#Form graph
for word in words:
    current = graph
    for letter in word:
        if not current.has_key(letter):
            current[letter] = {}
        current = current[letter]

for index, case in enumerate(testCases):
    print 'Case #%d: %d' % (index+1, formCases(case, graph))
