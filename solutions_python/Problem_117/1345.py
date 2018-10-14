height_min = 1
height_max = 100

def main():
  numCases = input()
  for case in xrange(1, numCases+1):
    rows, cols = input_line(int)
    this, currMin, currMax = get_case(rows)

    while min(min(this)) == currMin and currMin < currMax:
      validrows = list(find_rows(this, currMin, rows))
      validcols = list(find_cols(this, currMin, cols))
      for row in xrange(rows):
        if row in validrows:
          for n in xrange(len(this[row])):
            this[row][n] = currMin + 1
        for col in validcols:
          this[row][col] = currMin + 1
      currMin += 1

    result = min(min(this)) == currMax

    printCase(case, yes_no(result))


def find_rows(lawn, currMin, rows):
  matches = []
  for row in xrange(rows):
    if max(lawn[row]) == currMin:
      matches += [row]
  return matches


def find_cols(lawn, currMin, numcols):
  matches = []
  for col in xrange(numcols):
    match = True
    for line in lawn:
      if match == True and line[col] != currMin:
        match = False
    if match == True:
      matches += [col]
  return matches

def get_case(numrows):
  lawn = []
  minimum = height_max + 1
  maximum = height_min - 1
  for row in xrange(numrows):
    line = input_line(int)
    for n in line:
      if n < minimum:
        minimum = n
      if n > maximum:
        maximum = n
    lawn.append(line)
  return lawn, minimum, maximum

def increment(n):
  n += 1

def yes_no(boolval):
  if boolval:
    return "YES"
  else:
    return "NO"

def input_line(function=str):
  return map(function, raw_input().split())

def printCase(case, result):
  print 'Case #{0}: {1}'.format(case, result)

main();
