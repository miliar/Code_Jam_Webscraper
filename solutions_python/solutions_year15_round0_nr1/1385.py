import string

_file = open("./A-large.in")
# _file = open("./A-small-attempt0.in")
_result = open("./result.txt", "w")

datasetSize = int(_file.readline())

for i in range(datasetSize):
  peopleCount, peopleShiness = _file.readline().replace("\n", "").split(' ')
  peopleCount = int(peopleCount)
  peopleShiness = [int(number) for number in list(peopleShiness)]

  # print peopleCount, peopleShiness

  additionalPeople = 0
  availablePeople = 0

  for j in range(len(peopleShiness)):
    if availablePeople + additionalPeople < j:
      additionalPeople = j - availablePeople

    availablePeople += peopleShiness[j]

  result = "Case #" + str(i + 1) + ": " + str(additionalPeople)

  print result
  _result.write(result + "\n")

_file.close()
_result.close()
