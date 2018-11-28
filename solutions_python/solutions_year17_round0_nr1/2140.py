import string

#inputFile = open('large_input_test.in', 'r')
inputFile = open('pancakes.in', 'r')
inputData = inputFile.read().strip()

numCases  = int(inputData.split('\n')[0])
data      = inputData.split('\n')

def formatAnswer(index, answer):
    return "Case #" + str(index) + ": " + str(answer)

def parseInputConfig(config):
    return map(lambda x: x == '+', config)

def flopRange(config, start, k):
    end               = start + k
    for i in range(start, end):
        config[i] = not config[i]

def computeAnswer(config, k):
    config = parseInputConfig(config)
    count  = 0

    for i in xrange(len(config) - k+1):
        if False not in config:
            break
        
        if not config[i]:
            flopRange(config, i, k)
            count += 1

    if False in config:
        return "IMPOSSIBLE"

    return count


for case in xrange(1, numCases+1):

    config, k = data[case].split(" ")
    k         = int(k)
    answer    = computeAnswer(config, k)
    print formatAnswer(case, answer)

