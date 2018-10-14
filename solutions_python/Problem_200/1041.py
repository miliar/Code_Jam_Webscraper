
import sys

fname = sys.argv[1]

output_file = open("output.txt", "w")

def isTidy(num):
  if len(num) <= 1:
    return True

  lastNum = num[0]
  for i in range(0, len(num)):
    if num[i] < lastNum:
      return False
    lastNum = num[i]
  return True

def returnNines(num):
  ret = ""
  for i in xrange(0, num):
    ret += "9"
  return ret


def makeTidy(line):
  num = line[0]
  for i in range(1, len(line)):
    if not isTidy(line[:i+1]):
      num = makeTidy(str(int(num)-1)) + returnNines(len(line) - len(num))
      break
    else:
      num += line[i]
  return num

with open(fname) as f:
  next(f)
  count = 1
  for line in f:
    line = line.rstrip()
    output_file.write("Case #" + str(count) + ": " + makeTidy(line).lstrip("0") + "\n")
    count += 1

output_file.close()
