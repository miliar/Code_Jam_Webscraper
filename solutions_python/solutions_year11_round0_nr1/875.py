#!/usr/bin/python -tt

import sys

def doWork(order, orange, blue): 
  answer = 0
  orangePos = 1
  bluePos = 1
  nextOrange = 0
  nextBlue = 0
  #base case
  if len(orange) > 0: 
    nextOrange = orange.pop(0)
    orangePos = nextOrange
  if len(blue) > 0: 
    nextBlue = blue.pop(0)
    bluePos = nextBlue
  
  for next in order: 
    if next == 'O': 
      answer += nextOrange
      #print 'answer is: ', answer
      nextBlue = nextBlue - nextOrange
      if nextBlue < 1: 
        nextBlue = 1
      if len(orange) > 0: 
        nextOrange = abs(orange[0] - orangePos) + 1
        orangePos = orange.pop(0)
      else: 
        nextOrange = 0
      #print 'nextOrange', nextOrange
      #print 'nextBlue', nextBlue
    elif next == 'B': 
      answer += nextBlue
      #print 'answer is: ', answer
      nextOrange = nextOrange - nextBlue
      if nextOrange < 1: 
        nextOrange = 1
      if len(blue) > 0: 
        nextBlue = abs(blue[0] - bluePos) + 1
        bluePos = blue.pop(0)
        #print blue[0], 'asd', bluePos
      else:
        nextBlue = 0
      #print 'nextOrange', nextOrange
      #print 'nextBlue', nextBlue
    #print 'answer is: ', answer
    #print 'now'
    #print 'nextOrange', nextOrange
    #print 'nextBlue', nextBlue
  #print answer
  return answer


def main():
  f = open("A-large.in", 'rU')
  lines = f.readline()
  
  output = open('output', 'w')
  for i in range(int(lines)):
    line = f.readline().split(" ")
    order = []
    orange = []
    blue = []
    for (counter, color) in enumerate(line[1:]):
      if counter % 2 == 0:
        order.append(color)
        if color == 'O': 
          orange.append(int(line[1:][counter+1]))
        elif color == 'B': 
          blue.append(int(line[1:][counter+1]))
        else:
          print 'invalid color'
          return
    #print order
    #print 'orange', orange
    #print 'blue', blue
    #print 'Case #'+(str(i+1))+":", 
    output.write("Case #"+(str(i+1))+": ")
    #if (i == 2):
    #print doWork(order, orange, blue)
    output.write(str(doWork(order, orange, blue)))
    output.write("\n")
    #break
  f.close()
  output.close()
  
if __name__ == '__main__':
  main()
