import sys

def get_row(row_number):
  for i in range(row_number):
    line = sys.stdin.readline().strip()

  candidates = [int(i) for i in line.split(" ")]
  for i in range(4-row_number):
    sys.stdin.readline()

  return candidates

test_cases = int(sys.stdin.readline().strip())

for test_case in range(test_cases):
  row_number = int(sys.stdin.readline().strip())
  candidates = get_row(row_number)

  row_number = int(sys.stdin.readline().strip())
  second_choice = get_row(row_number)

  guesses = list(set(candidates) & set(second_choice))

  if len(guesses) == 1:
    resp = guesses[0]
  elif len(guesses) == 0:
    resp = "Volunteer cheated!"
  else:
    resp = "Bad magician!"

  print "Case #{0}: {1}".format(test_case+1, resp)
