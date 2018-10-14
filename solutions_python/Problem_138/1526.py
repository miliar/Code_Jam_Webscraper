#!/usr/bin/python

'''
Deceitful War
'''
def deceitful_war (filename):
  inFile = open (filename, 'r')
  outFile = open ('output.out', 'w')

  numcase = int (inFile.readline ().strip ())
  for i in range (0, numcase):
    inFile.readline ()

    line = (inFile.readline ().strip ())
    naomi = [float(x) for x in line.split(' ')]
    naomi.sort ()
    naomi_orig = []
    for x in naomi:
      naomi_orig.append (x)

    line = (inFile.readline ().strip ())
    ken =  [float(x) for x in line.split(' ')]
    ken.sort ()
    ken_orig = []
    for x in ken:
      ken_orig.append (x)

    good_score = 0
    deceive_score = 0

    while len (naomi) > 0:
      naomi_item = naomi[0]
      # Search KEN for smallest thing larger than naomi
      ken_index = 0
      flag = False
      for x in range (0, len (ken)):
        ken_index = x
        if ken[ken_index] >= naomi_item:
          flag = True
          break

      if flag is False:
        good_score += 1

      del naomi[0]
      del ken[ken_index]

    naomi = naomi_orig
    ken = ken_orig

    print naomi
    print ken

    # Deceive score
    while len (naomi) > 0:
      # I know ken's biggest
      naomi_item = naomi[-1]
      ken_index = 0
      flag = False
      for x in range (len (ken) - 1, -1, -1):
        ken_index = x
        if ken[ken_index] <= naomi_item:
          flag = True
          break

      if flag is True:
        deceive_score += 1

      del naomi[-1]
      del ken[ken_index]

    outFile.write ("Case #" + str (i + 1) + ": " + str (deceive_score) + " " + str (good_score) + "\n")

  outFile.close ()
  inFile.close ()

def main ():
  deceitful_war ("D-large.in")
main ()