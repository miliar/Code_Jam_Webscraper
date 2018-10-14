import string

# _file = open("./D-small-attempt0.in")
_file = open("./D-large.in")
_result = open("./result.txt", "w")

dataset_size = int(_file.readline())
case = 0

for i in range(dataset_size):
  case += 1

  total = int(_file.readline()) # number of cubes
  naomiSet = sorted(map(lambda x: float(x), _file.readline().replace("\n", '').split(' ')))
  kenSet = sorted(map(lambda x: float(x), _file.readline().replace("\n", '').split(' ')))
  _kenSet = list(kenSet) # cache

  # print naomiSet
  # print kenSet

  war1 = 0
  war2 = 0

  # War1 (naive)
  for cube1 in naomiSet:
    found = False
    for cube2 in kenSet:
      if cube2 > cube1:
        kenSet.remove(cube2)
        found = True
        break
    if found != True:
      war1 += 1
      del kenSet[0]

  # War2 (smart)
  for cube1 in naomiSet:
    if cube1 < _kenSet[0]:
      # remove the biggest cube
      _kenSet.pop()
    else:
      # remove the smallest cube
      _kenSet.pop(0)
      war2 += 1

  result = "Case #" + str(case) + ": " + str(war2) + ' ' + str(war1)

  print result
  _result.write(result + "\n")

_file.close()
_result.close()
