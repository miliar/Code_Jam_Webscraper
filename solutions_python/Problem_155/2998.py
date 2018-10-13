fname = r'C:\Users\Jambalaya\Dropbox\Programming\codejam practice\Audience\A-large.in'
outfname = r'C:\Users\Jambalaya\Dropbox\Programming\codejam practice\Audience\output.in'


outputFile = open(outfname,'w')
outputFile.truncate()

with open(fname) as f:
    content = f.readlines()

testCases = int(content[0])

for i in range(testCases):
    splitPoint = content[i+1].find(' ')
    shynessMax = int(content[i+1][:splitPoint])

    shynessString = content[i+1][splitPoint+1:].rstrip('\n')
    shynessList = []
    for char in shynessString:
        shynessList.append(int(char))

    shynessLevel = 0
    clappers = 0
    friendsInvited = 0

    for potentialClappers in shynessList:
        if clappers >= shynessLevel:
            clappers += potentialClappers
        else:
            friendsNeeded = (shynessLevel - clappers)
            friendsInvited += friendsNeeded
            clappers += potentialClappers + friendsNeeded

        shynessLevel += 1


    
    output = "Case #" + str(i + 1) + ": " + str(friendsInvited)
    
    outputFile.write(output + '\n')
    print output

outputFile.close()
    