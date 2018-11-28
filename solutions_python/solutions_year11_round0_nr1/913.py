#!/usr/bin/python

import sys


class ButtonOrder:
  def __init__(self, number, button):
    self.number = number
    self.button = button

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    # reading data
    inputs = input.readline().rstrip().split()

    blueList = []
    oranList = []

    for i in range(0, int(inputs[0])):
      order = ButtonOrder(i, int(inputs[1+(i*2)+1]))
      if (inputs[1+(i*2)] == 'O'):
        oranList.append(order)
      else:
        blueList.append(order)

    currentId = 0

    bluePosition = 1
    oranPosition = 1

    nbMoves = 0

    while True:
      if (len(blueList) == 0 and len(oranList) == 0):
        break

      prevId = currentId

      if (len(blueList) > 0):
        if (bluePosition != blueList[0].button):
          if (bluePosition < blueList[0].button):
            bluePosition += 1
          else:
            bluePosition -= 1
        elif blueList[0].number == prevId:
          blueList.pop(0)
          currentId += 1
      if (len(oranList) > 0):
        if (oranPosition != oranList[0].button):
          if (oranPosition < oranList[0].button):
            oranPosition += 1
          else:
            oranPosition -= 1
        elif oranList[0].number == prevId:
          oranList.pop(0)
          currentId += 1

      nbMoves += 1

    output.write('Case #%d: %s\n' % (val,nbMoves))

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
