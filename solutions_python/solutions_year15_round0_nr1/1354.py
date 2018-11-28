f = open('A-large.in', 'r')
output = open('output.txt', 'w')
numTrials = int(f.readline())
counter = 0
zerocounter = 0
line = 0

for Trial in f:
    line+=1
    MaxShyness = int(Trial[:Trial.find(' ')])
    Audience = Trial[Trial.find(' ') + 1:].replace('\n', '')
    for c in Audience:
        if int(c) + counter > 0:
            counter += int(c) - 1
        else:
            zerocounter += 1
    outputline = str("Case #" + str(line) + ": " + str(zerocounter) + "\n")
    output.write(outputline)
    zerocounter = 0
    counter = 0
output.close()



