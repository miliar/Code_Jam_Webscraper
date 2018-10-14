caseData = [lines.rstrip() for lines in open('standingOvation.in', 'r')]
fileOut = open('standingOvation.out', 'w')

for case in range(int(caseData[0])):
    standing = 0
    friends = 0
    shyMax, audience = caseData[case+1].split()
    for iter, shyLevel in enumerate(audience):
        if standing >= iter:
            standing += int(shyLevel)
        else:
            standing += (iter)-standing
            friends += 1
            standing += int(shyLevel)
    fileOut.write('Case #'+str(case+1)+': '+str(friends)+'\n')

fileOut.close()