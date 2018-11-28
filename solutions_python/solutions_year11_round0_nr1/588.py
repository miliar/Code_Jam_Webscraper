import os

def minimizeMoves(buttons):
  orangeButtons = [b[1] for b in buttons if b[0] == 'O']
  blueButtons = [b[1] for b in buttons if b[0] == 'B']
  steps = 0
  orangeCurPosition = 1
  blueCurPosition = 1
  curSeqPos = 1
  for i,b in enumerate(buttons):
    orange_steps = 0
    blue_steps = 0
    if orangeButtons and orangeCurPosition != orangeButtons[0]:
      orange_steps = abs(orangeCurPosition - orangeButtons[0])
    if blueButtons and blueCurPosition != blueButtons[0]:
      blue_steps = abs(blueCurPosition - blueButtons[0])
    if b[0] == 'O':
      steps += orange_steps
      orangeCurPosition = orangeButtons[0]
      orangeButtons = orangeButtons[1:]
      if blue_steps > orange_steps:
        blueCurPosition += -orange_steps-1 if blueCurPosition > blueButtons[0] else orange_steps+1
      elif blue_steps:
        blueCurPosition = blueButtons[0]
    else:
      steps += blue_steps
      blueCurPosition = blueButtons[0]
      blueButtons = blueButtons[1:]
      if blue_steps < orange_steps:
        orangeCurPosition += -blue_steps-1 if orangeCurPosition > orangeButtons[0] else blue_steps+1
      elif orange_steps:
        orangeCurPosition = orangeButtons[0]
    steps += 1
#    print "step %s: Button %s: O: %s: B: %s" % (steps, b[1], orangeCurPosition, blueCurPosition)
#    print orange_steps, blue_steps
  return steps

def main():
  infile = open("bottrust.in", "r", True)
  inputs = infile.readlines()
  cases = int(inputs[0].strip())
  for j in xrange(1,cases+1):
    sequence = inputs[j].split()
    length = int(sequence[0].strip())
    sequence = sequence[1:]
    buttons = [(sequence[2*i].strip(), int(sequence[(2*i) + 1].strip())) for i in xrange((length))]
#    print buttons
    moves = minimizeMoves(buttons)
    print "Case #%s: %s" % (j, moves)

if __name__ == '__main__':
  main()
