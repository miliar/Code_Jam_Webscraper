T = int(raw_input())
for t in range(T):
  output = "Case #" + str(t+1) + ": "
  row1 = int(raw_input())
  table1 = []
  for i in range(4):
    line = raw_input()
    table1.append(line.split(' '))
  row2 = int(raw_input())
  table2 = []
  for i in range(4):
    line = raw_input()
    table2.append(line.split(' '))

  count = 0
  ch = '0'
  for c1 in table1[row1-1]:
    for c2 in table2[row2-1]:
      if c1 == c2:
        count += 1
        ch = c1
  if count == 0:
    output += "Volunteer cheated!"
  elif count == 1:
    output += ch
  else:
    output += "Bad magician!"
  print output
