firstLine = 1
numLines = 0
lineIndex = 0
i = 0
input = open('input.txt', 'r')
output = open('output.txt', 'r')
a = output.readlines()
toEnglish = {'z':'q', 'q':'z'}
for line in input:
    if firstLine == 1:
        numLines = int(line)
        #print numLines
        firstLine = firstLine+1
    else:
        i = 0
        for letterInput in line:
            letterOutput = a[lineIndex][i]
            print lineIndex
            toEnglish[letterInput] = letterOutput
            print toEnglish
            i = i+1;
        lineIndex=lineIndex+1
print toEnglish['e']
input.close()
input2 = open('A-small-attempt0.in', 'r')
output2 = file('output2.txt', 'w')
n = 1
cases = 10
first = 1
newLine = ' '
for line in input2:
    if first == 1:
        print n
        cases = int(line)
        first = first+1
    else:
        for letter in line:
            newLine+=toEnglish[letter]
        print newLine
        output2.write('Case #' + str(n) + ':'+ newLine)
        n += 1
        newLine = ' '
input2.close()
output.close()
output2.close()