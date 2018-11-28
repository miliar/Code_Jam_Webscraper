fin = "A-small-attempt0.in"
fout = "A-small-attempt0.out"

with open(fout, "wt") as out_file:
  with open(fin, "rt") as in_file:
    num_cases = int(in_file.readline())

    for case_no in range(num_cases):
      A = int(in_file.readline())
      arrangement = []
      for i in range(4):
        line = in_file.readline().rstrip('\n')
        arrangement.append(line.split(' '))

      cards1 = arrangement[A-1]
      
      B = int(in_file.readline())
      arrangement = []
      for i in range(4):
        line = in_file.readline().rstrip('\n')
        arrangement.append(line.split(' '))
      
      cards2 = arrangement[B-1]

      card = set(cards1) & set(cards2)
      
      if len(card) == 0:
        out_file.write("Case #%d: %s\n" % (case_no + 1, "Volunteer cheated!"))
      elif len(card) > 1:
        out_file.write("Case #%d: %s\n" % (case_no + 1, "Bad magician!"))
      else:
        c = card.pop()
        out_file.write("Case #%d: %s\n" % (case_no + 1, c))
