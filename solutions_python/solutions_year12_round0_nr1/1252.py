import string

# Build dictionary
fcode = file('gcode', 'rw')
feng = file('english', 'rw')

codelines = fcode.readlines()
englines = feng.readlines()

# Empty dictionary to hold code to english mapping
codeToEng = {}

for i in range(0,3):
    # print i
    for idx, letter in enumerate(codelines[i]):
        # print letter + str(idx) + englines[i][idx]
        if letter in codeToEng:
            continue
        elif (letter == ' ') or (letter == '\n'):
            continue
        else:
            # Add mapping to dictionary if not in there
            codeToEng[letter] = englines[i][idx]

# Add space and mapping not found in example
codeToEng[' '] = ' '
codeToEng['q'] = 'z'
codeToEng['z'] = 'q'
print codeToEng

fcode.close()
feng.close()

# Now translate input text

fin = file('A-small-attempt0.in', 'rw')
output = file('output.txt','w')
               
numLine = 0   
for line in fin:
    if numLine == 0:
        numLine = numLine + 1
    else:
        output.write('Case #' + str(numLine) + ': ')
        sentenceList = []
        for letter in line:
            if letter == '\n':
                continue
            translatedLetter = codeToEng[letter]
            # print translatedLetter + '\n'
            sentenceList.append(translatedLetter)

        numLine = numLine + 1
        output.write(''.join(sentenceList))
        output.write('\n')

fin.close()
output.close()



