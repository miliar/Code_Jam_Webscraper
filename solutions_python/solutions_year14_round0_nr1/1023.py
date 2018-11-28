from os import sys

def get_int():
  return int(sys.stdin.readline())

def get_row(row_num):
  row = None
  for i in range(1,4+1):
    raw_row = sys.stdin.readline()
    if (i == row_num):
      row = set([int(s) for s in raw_row.split()])
  return row

num_cases = get_int()

for case in range(1,num_cases+1):
  rows = []
  for i in range(2):
    row_num = get_int()
    rows.append(get_row(row_num))
  cards = rows[0].intersection(rows[1])
  message = ""
  if len(cards) == 0:
    message = "Volunteer cheated!"
  elif len(cards) == 1:
    message = str(list(cards)[0])
  else:
    message = "Bad magician!"

  print "Case #" + str(case) + ":", message
