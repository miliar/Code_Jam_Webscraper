import sys


f = open(sys.argv[1], "r")

cases = f.readline()

for case in range(int(cases)):
  first_row = int(f.readline())

  for i in range(4):
    row = f.readline()
    ns = list(row.strip().split())
    if (i == first_row-1):
      full_row_one = []
      for j in range(4):
        full_row_one.append(int(ns[j]))


  second_row  = int(f.readline())

  for i in range(4):
    row = f.readline()
    ns = list(row.strip().split())
    if (i == second_row-1):
        full_row_two = []
        for j in range(4):
          full_row_two.append(int(ns[j]))

  match = 0
  number_match = 0
  for num in full_row_one:
    n = num
    if(n in full_row_two):
      number_match = n
      match = match + 1

  if (match == 1):
    print "Case #"+str(case+1)+": "+ str(number_match)

  if (match > 1):
    print "Case #"+str(case+1)+": Bad magician!"

  if(match == 0):
    print "Case #"+str(case+1)+": Volunteer cheated!"
