mapping = {'y': 'a', 'e': 'o', 'q': 'z', ' ': ' '}
alphabet = list('abcdefghijklmnopqrstuvwxyz')


def train(inputFile, outputFile):
    cases = readInput(inputFile)
    results = readOutput(outputFile)
    for idx in range(len(cases)):
        trainCase(cases[idx], results[idx])
    

def readInput(inputFile):
    lines = int(inputFile.readline())
    cases = [];
    for _ in range(lines):
        cases.append(inputFile.readline().strip())
    return cases

def readOutput(outputFile):
    results = []
    for line in outputFile:
        results.append(line.split(': ')[1].strip())
    return results

def trainCase(case, result):
    for idx in range(len(case)):
        key = case[idx]
        value = result[idx]
        putMapping(key, value)
    
def translate(googlerese):
    global mapping
    english = ''
    for idx in range(len(googlerese)):
        frm = googlerese[idx]
        english += mapping[frm]
    return english

def printMapping():
    global mapping
    print mapping

def putMapping(key, value):
    global mapping
    if key in mapping and value != mapping[key]:
        raise Exception('Contradiction')
    else:
        mapping[key] = value
    
def isComplete():
    global mapping
    return len(mapping) == 27

def completeMapping():
    global mapping
    if len(mapping) < 26:
        raise Exception('Guess is not possible')
    elif len(mapping) == 27:
        return
    
    missingKey = None
    missingValue = None
    
    for x in alphabet:
        if not x in mapping:
            missingKey = x
            break
        
    for x in alphabet:
        if not x in mapping.values():
            missingValue = x
            break
        
    if missingKey != None and missingValue != None:
        putMapping(missingKey, missingValue)

def translateFiles(inputFile, outputFile):
    cases = readInput(inputFile)
    for idx in range(len(cases)):
        result = 'Case #%d: %s\n' % (idx + 1, translate(cases[idx]))
        outputFile.write(result)

def trainUsingExample():
    exampleInput = open('example.in')
    exampleOutput = open('example.out')
    train(exampleInput, exampleOutput)
    exampleInput.close()
    exampleOutput.close()
    completeMapping()         

def solveProblem():
    problemInput = open('A-small-attempt0.in')
    problemOutput = open('A-small-attempt0.out', 'w')
    translateFiles(problemInput, problemOutput)
    problemInput.close()
    problemOutput.close()
    
if __name__ == '__main__':
    trainUsingExample()
    solveProblem()
    
