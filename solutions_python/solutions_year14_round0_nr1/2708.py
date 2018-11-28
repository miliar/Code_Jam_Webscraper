#!/usr/local/bin/python2.7
    
f = open('input.txt','r')
line = f.readline().strip()
number_of_cases = int(line)
for case in range(number_of_cases):
  print 'Case #'+str(case+1)+':',
  row_1 = int(f.readline().strip())
  for row in range(4):
    line = f.readline().strip()
    if row+1 == row_1:
      first_row = line
  row_2 = int(f.readline().strip())
  for row in range(4):
    line = f.readline().strip()
    if row+1 == row_2:
      second_row = line
  first_row = first_row.split(' ')
  second_row = second_row.split(' ')
  cross = [x for x in first_row if x in second_row]
  if len(cross)>1:
    print 'Bad magician!',
  elif len(cross)==1:
    print int(cross[0]),
  else:
    print 'Volunteer cheated!',
  print ''