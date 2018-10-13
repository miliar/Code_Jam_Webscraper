import string, math

#inputFile = open('large_input_test.in', 'r')
inputFile = open('A-large.in', 'r')
inputData = inputFile.read().strip()

numCases  = int(inputData.split('\n')[0])
data      = inputData.split('\n')

def formatAnswer(index, answer):
  return "Case #" + str(index) + ": " + str(answer)


def computeAnswer(horses, dist):
    longestTime = 0
    for horse in horses:
        distLeft = dist - horse[0]
        speed    = horse[1] * 1.0
        timeTaken = distLeft / speed
        if timeTaken > longestTime:
            longestTime = timeTaken
    return round(dist / longestTime, 8)


index = 1
for case in xrange(1, numCases+1):
    dist, numHorses  = map(int, data[index].split(" "))

    horses  = map(lambda row: map(int, row.split(" ")), data[index+1: index+numHorses+1])

    index  += numHorses + 1
    answer  = computeAnswer(horses, dist)

    print formatAnswer(case, answer)


