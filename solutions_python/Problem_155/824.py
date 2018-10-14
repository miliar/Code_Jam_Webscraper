#file('C-large-practice.in').read()
#

almost1 = 1.0 - 1e-8
almost0 = 1e-8

def processAllInput(text, toFile = False):
    fileName = text
    if toFile:
        text = file(fileName).read()
    finalResult = []
    numTests = int(text.split('\n')[0])
    lines = text.split('\n')
    for i in range(numTests):
        #Problem-specific code starts here############
        
        message = lines[i+1]
        ovators = message.split(' ')[1]
        ovators = list(map(int, ovators))

        neededFriends = 0;
        totalStanding = 0;

        for x, j in enumerate(ovators):
            if totalStanding < x:
                neededFriends = max([neededFriends, x - totalStanding])
            totalStanding += j
                    

            
        line = 'Case #{0}: {1}'.format(i+1, neededFriends)
        
        #Problem-specific code ends here##############
        if not toFile:
            print line
        finalResult.append(line)
    if toFile:
        file(fileName.split('.')[0]+'.out', 'w').write('\n'.join(finalResult))
