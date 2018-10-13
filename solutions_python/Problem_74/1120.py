import sys
import re

def calculate(dataset):
  Orange = []
  Blue = []
  for i in xrange(int(dataset[0])):
    if dataset[2*(i + 1) - 1] == 'O':
      Orange.append(dataset[2*(i + 1)])
    elif dataset[2*(i + 1) - 1] == 'B':
      Blue.append(dataset[2*(i + 1)])
    else:
      return false

  nowOrange = 1
  nowBlue = 1

  orangeIndex = 0
  blueIndex = 0

  count = 0
  bButton = False
  oButton = False

  for i in xrange(int(dataset[0])):
    while True:
      if dataset[2*(i + 1) - 1] == 'O':
        if nowOrange == int(Orange[orangeIndex]):
          orangeIndex += 1
          oButton = True
      elif dataset[2*(i + 1) - 1] == 'B':
        if nowBlue == int(Blue[blueIndex]):
          blueIndex += 1
          bButton = True

      if not oButton:
        if len(Orange) > orangeIndex:
          if nowOrange != int(Orange[orangeIndex]):
            if nowOrange < int(Orange[orangeIndex]):
              nowOrange += 1
            elif nowOrange > int(Orange[orangeIndex]):
              nowOrange -= 1

      if not bButton:
        if len(Blue) > blueIndex:
          if nowBlue != int(Blue[blueIndex]):
            if nowBlue < int(Blue[blueIndex]):
              nowBlue += 1
            elif nowBlue > int(Blue[blueIndex]):
              nowBlue -= 1
      count += 1
      if bButton or oButton:
        bButton = False
        oButton = False
        break
  return count

if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise "please file name"
  r = re.compile('[\ \n]')

  try:
    fi = open(sys.argv[1], "r")
    lineNum = fi.readline()
    if lineNum > 0:
      for i in xrange(int(lineNum)):
        line = fi.readline()
        dataset =  r.split(line)
        print "Case #%d: %d" %(i+1, calculate(dataset))
  except IOError, inst:
    print inst
  finally:
    if fi: fi.close()

