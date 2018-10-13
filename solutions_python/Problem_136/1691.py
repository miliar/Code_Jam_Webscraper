import string

_file = open("./B-small-attempt0.in")
_result = open("./result.txt", "w")

dataset_size = int(_file.readline())
case = 0

for i in range(dataset_size):
  case += 1


  Price, Rate, Target = map(lambda x: float(x), _file.readline().replace("\n", "").split(' '))
  minTime = Target / 2.0

  # print Price, Rate, Target, minTime

  farms = 0
  while(True):
    farms += 1
    time = 0
    rate = 2

    for f in range(farms):
      time += Price / rate
      rate += Rate

    time += Target / rate

    # print time, rate, minTime

    if time < minTime:
      minTime = time
    else:
      break

  result = "Case #" + str(case) + ": " + str(round(minTime, 7))

  print result
  _result.write(result + "\n")

_file.close()
_result.close()
