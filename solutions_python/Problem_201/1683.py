import sys
import math

# ----- debug --------
debug = False
def mprint(mstr):
  if(debug): print(mstr)

# ----- debug --------

def solve_last_step(size):
  mprint("solve_last_step: size: " + str(size))
  nval1 = math.floor(size/2.0)
  nval2 = math.ceil(size/2.0) - 1
  res = str(nval1) + " " + str(nval2)
  mprint("result: " + str(res))
  return res

def solve_step(ranges, k, step):
  mprint('\n1. inside solve_step k: ' + str(k) + ' vals: ' + str(ranges) + " step: " + str(step))
  newRanges = {}
  sortedKeys = list(ranges.keys())
  sortedKeys.sort()
  for key in reversed(sortedKeys):
    value = ranges[key]
    mprint('2.1. inside solve_step k: ' + str(k) + ' newRanges: ' + str(newRanges) + ' value: ' + str(value) + " key: " + str(key))
    ## find the new values by dividing it
    step += ranges[key]

    nval1 = math.floor(key/2.0)
    nval2 = math.ceil(key/2.0) - 1
    mprint("2.2 nval1: " + str(nval1) + " nval2: " + str(nval2) + " value: " + str(value) + " step: " + str(step))

    ## found new range
    if nval1 not in newRanges: newRanges[nval1] = 0
    newRanges[nval1] += value

    if nval2 not in newRanges: newRanges[nval2] = 0
    newRanges[nval2] += value

    mprint('2.3. inside solve_step k: ' + str(k) + ' newRanges: ' + str(newRanges) + ' value: ' + str(value) + " key: " + str(key) + " step: " + str(step))
    if(step >= k):
      return str(nval1) + " " + str(nval2) #solve_last_step(nval1)
      # return solve_from_dictionary(newRanges, ranges)
    ##
  return solve_step(newRanges, k, step)

def solve_from_dictionary(x, y):
  z = {**x, **y}
  keys = list(z.keys())
  keys.sort()
  return solve_last_step(keys[-1])

def solve(n, k):
  ranges = {n:1}
  res = solve_step(ranges, k, 0)
  mprint("res: " + str(res))
  return res

def main():
  ## get the file
  filename = sys.argv[1]
  fileReader = open(filename, 'r')
  numLines = int(fileReader.readline())
  num = 1;
  for line in fileReader:
    if(num > numLines): break
    data = line.split()
    result = solve(int(data[0]), int(data[1]))
    finalString = "Case #" + str(num) + ": " + str(result)
    num += 1
    print(finalString)

main()
