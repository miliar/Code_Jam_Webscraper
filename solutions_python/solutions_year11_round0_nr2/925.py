#!/usr/bin/python

import sys
from sets import Set


# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    # reading data
    inputs = input.readline().rstrip().split()

    id = 0

    comb = {}
    oppo = {}
    oppoLetter = Set([])
    currentOppo = {}
    result = []

    combCount = int(inputs[id])
    id += 1

    for i in range(id, id + combCount):
      s = inputs[id]
      comb[min(s[0], s[1]) + max(s[0], s[1])] = s[2]
      id += 1

    opposCount = int(inputs[id])
    id += 1

    for i in range(id, id + opposCount):
      s = inputs[id]
      oppo[min(s[0], s[1]) + max(s[0], s[1])] = True
      oppoLetter.add(s[0])
      oppoLetter.add(s[1])
      id += 1

    id += 1
    inputStr = inputs[id]
    result.append(inputStr[0])
    if (result[0] in oppoLetter):
      currentOppo[result[0]] = 1

    for x in inputStr[1:]:
      try:
        lastLetter = result[-1]
        newLetter = comb[min(x, lastLetter) + max(x, lastLetter)]
        try:
          currentOppo[lastLetter] -= 1
        except KeyError:
          pass
        result[-1] = newLetter
        continue
      except KeyError:
        pass
      except IndexError:
        pass

      cleared = False
      if x in oppoLetter:
        for y in currentOppo:
          if currentOppo[y] > 0 and min(x, y) + max(x, y) in oppo:
            result = []
            currentOppo.clear()
            cleared = True
            break
        if cleared:
          continue
        try:
          currentOppo[x] += 1
        except KeyError:
          currentOppo[x] = 1

      result.append(x)

    res = str(result)
    res = str.replace(res, "'", "")

    output.write('Case #%d: %s\n' % (val,res))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "Need file as argument"
    sys.exit(1)

  input_file = sys.argv[1]

  # open the file
  input_handler = open(input_file, 'r')
  output_handler = open(input_file + '.out', 'w+')

  process(input_handler, output_handler)

  # close files
  input_handler.close()
  output_handler.close()
