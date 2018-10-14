import string

_file = open("./A-small-attempt0.in")
_result = open("./result.txt", "w")

dataset_size = int(_file.readline())
row1 = [0 for x in range(4)]
row2 = [0 for x in range(4)]
case = 0

def diff(a, b):
  b = set(b)
  return [aa for aa in a if aa in b]

for i in range(dataset_size):
  case += 1

  selected_row = int(_file.readline()) - 1 # convert to 0 based index
  for j in range(4):
    if j == selected_row:
      row1 = list(_file.readline().replace("\n", "").split(' '))
    else:
      _file.readline()

  selected_row = int(_file.readline()) - 1 # convert to 0 based index
  for j in range(4):
    if j == selected_row:
      row2 = list(_file.readline().replace("\n", "").split(' '))
    else:
      _file.readline()

  # print row1
  # print row2

  diff_row = diff(row1, row2)
  # print diff_row

  if len(diff_row) == 1:
    result = "Case #" + str(case) + ": " + str(diff_row[0])
  elif len(diff_row) > 1:
    result = "Case #" + str(case) + ": Bad magician!"
  else:
    result = "Case #" + str(case) + ": Volunteer cheated!"

  print result
  _result.write(result + "\n")

  # print gameResult(matrix)

_file.close()
_result.close()
