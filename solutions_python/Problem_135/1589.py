#!/usr/bin/python

def magic_trick (filename):
  inFile = open (filename, 'r')
  outFile = open ('output.out', 'w')

  numcase = int (inFile.readline ().strip ())
  for i in range (0, numcase):
    row0 = int (inFile.readline ().strip ())
    vals0 = set ()
    # Read rows
    for j in range (0, 4):
      line = inFile.readline ().strip ()
      row = [int(x) for x in line.split(' ')]
      if row0 == j + 1:
        for x in row:
          vals0.add (x);
    # Second round
    row1 = int (inFile.readline ().strip ())
    vals1 = set ()
    for j in range (0, 4):
      line = inFile.readline ().strip ()
      row = [int(x) for x in line.split(' ')]
      if row1 == j + 1:
        for x in row:
          vals1.add (x);

    count = 0
    num = 0
    for n in vals0:
      if n in vals1:
        count += 1
        num = n

    outFile.write ("Case #" + str (i + 1) + ": ")
    if count == 0:
      outFile.write ("Volunteer cheated!")
    elif count == 1:
      outFile.write (str (num))
    else:
      outFile.write ("Bad magician!")
    outFile.write ("\n")

  outFile.close ()
  inFile.close ()

def main ():
#  bad_horse ("A-small-practice-2.in");
#  do_moist ("C-small-practice-2.in")
#  phone_number ("A-large-practice.in")
#  wierd_sorting ("C-large-practice (1).in")
  magic_trick ("A-small-attempt0.in")

main ()