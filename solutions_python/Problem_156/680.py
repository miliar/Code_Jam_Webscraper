#file('C-large-practice.in').read()
#


def processAllInput(text, toFile = False):
    fileName = text
    if toFile:
        text = file(fileName).read()
    finalResult = []
    numTests = int(text.split('\n')[0])
    lines = text.split('\n')
    for i in range(numTests):
        #Problem-specific code starts here############
        
        message = lines[2*i+1:2*i+3]
        numDiners = int(message[0])

        theProblem = map(int, message[1].split(' '))
        theProblem.sort()

        foundAnswers = set()

        for eating in range(1, max(theProblem)+1):
            splitting = 0
            for plate in theProblem:
                splitting += int((plate-1)/eating)
            #print "With {0} eating, solved in {1}".format(eating, splitting + eating)
            foundAnswers.add(splitting + eating)

        
        line = 'Case #{0}: {1}'.format(i+1, min(foundAnswers))
        
        #Problem-specific code ends here##############
        if not toFile:
            print line
        finalResult.append(line)
    if toFile:
        file(fileName.split('.')[0]+'.out', 'w').write('\n'.join(finalResult))
