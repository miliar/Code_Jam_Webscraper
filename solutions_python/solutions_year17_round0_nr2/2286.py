import string

#inputFile = open('large_input_test.in', 'r')
inputFile = open('tidy-num.in', 'r')
inputData = inputFile.read().strip()

data      = map(lambda x: int(x), inputData.split('\n'))
numCases  = data[0]

def formatAnswer(index, answer):
  return "Case #" + str(index) + ": " + str(answer)

def computeAnswer(number):
    if int(string.join(sorted(str(number)), '')) == number:
        return number

    strN = str(number)
    n    = [int(x) for x in str(number)]

    for i in xrange(len(n)-1):
        if n[i] > n[i+1]:
            result = int(strN[:i+1]) * 10**(len(n) - i -1) - 1

    return computeAnswer(result)


for case in xrange(1, numCases+1):
  answer = computeAnswer(data[case])
  print formatAnswer(case, answer)


