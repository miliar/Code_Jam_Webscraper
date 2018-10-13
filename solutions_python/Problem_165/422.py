import string

# _file = open("./A-large.in")
_file = open("./A-small-attempt0.in")
_result = open("./result.txt", "w")

datasetSize = int(_file.readline())

for i in range(datasetSize):
  rows, columns, shipWidth = map(lambda x: int(x), _file.readline().replace("\n", "").split(' '))
  movements = 0

  # If number of columns is equal to ship width then we don't need one additional shoot
  movements = (columns / shipWidth) + shipWidth + (-1 if columns % shipWidth == 0 else 0)
  movements *= rows

  result = "Case #" + str(i + 1) + ": " + str(movements)

  print result
  _result.write(result + "\n")

_file.close()
_result.close()
