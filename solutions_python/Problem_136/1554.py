#!/usr/bin/python

'''
Cookie Clicker Alpha
'''

def cookie_clicker_alpha (filename):
  inFile = open (filename, 'r')
  outFile = open ('output.out', 'w')

  numcase = int (inFile.readline ().strip ())
  for i in range (0, numcase):
    line = (inFile.readline ().strip ())
    lst = [float(x) for x in line.split(' ')]
    C = lst[0]
    F = lst[1]
    X = lst[2]

#    print "C:", C, "F:", F, "X:", X
    rate = 2.0
    total_time = 0.0

    while (True):
      # Straight shot time
      strait_shot_time = (X / rate) + total_time
      # Time to buy some shit
      time_buy_farm = (C / rate) + (X / (rate + F)) + total_time

      if time_buy_farm < strait_shot_time:
        total_time += (C / rate)
        rate += F
      else:
        total_time = strait_shot_time
        break

    outFile.write ("Case #" + str (i + 1) + ": ")
    outFile.write (str (total_time) + '\n')
#    outFile.write (str (round (total_time, 7)) + '\n')

def main ():
  cookie_clicker_alpha ("B-large.in")

main ()