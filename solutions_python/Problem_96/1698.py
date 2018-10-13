## Google code jam round 2

## Thomas Raway

## dance
## input file should be something.in

text = open('B-large.in','r')
output = open('round2Output.txt','w')

line = text.readline()
numCases = int(line)

numberCase = 0

for line in text.readlines():
    numberCase += 1
    splitLine = line.split()
    numDancers = int(splitLine[0])
    numSurprise = int(splitLine[1])
    p = int(splitLine[2])

    numSpecial = 0
    accepted = 0

    for i in range(numDancers):
        totalScore = int(splitLine[3 + i])
        remainder = totalScore%3
        mainNumber = totalScore/3

        scores = []
        #i can take advantage of the score structure
        #the first score will always be the highest
        for i in range(3):
            scores.append(mainNumber)
        for i in range(remainder):
            scores[i] += 1

        #basic scores are set up
        #run permutations until the best is greater than p
        #or its lowest and highest number have a diff of 3
        #keep track of the number of suprisings, if we get over the number allowed
        #... then it doesn't count if its diff is 2

        flag = 0
        switch = 0
        while flag == 0:
            maxScore = scores[0]
            minScore = scores[1]

            diff = maxScore - minScore

            if(diff == 3):#meaning not possible
                break
            
            if(maxScore >= p):#meaning passed
                if(diff == 2):#meaning a surprise
                    if(numSpecial != numSurprise):
                        numSpecial += 1
                        accepted += 1
                        break
                    else:
                        break
                else:#meaning not a surprise
                    accepted += 1
                    break

            if(switch == 0):
                switch = 1
                if(scores[1] == 0 or scores[0] == 10):
                    break
                else:
                    scores[1] -= 1
                    scores[0] += 1

            else:
                switch = 0
                if(scores[2] == 0 or scores[0] == 10):
                    break
                else:
                    scores[2] -= 1
                    scores[0] += 1


            
    output.write('Case #%d: %d\n' %(numberCase, accepted))

        
        
text.close()
output.close()
