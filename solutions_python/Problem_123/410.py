#! /usr/bin/env python3

def findMinimum(cur, other, count):
  #print("cur {0}, other {1}, count {2}".format(cur, other, count))
  if len(other) == 0:
    return count
  if other[0] < cur:
    return findMinimum(cur + other[0], other[1:], count)
  else:
    if cur == 1:
      return count + len(other)
    minimum = findMinimum(cur * 2 - 1, other, count + 1)
    if minimum > len(other) + count:
      return count + len(other)
    else:
      return minimum

def processCase(i):
  line = input()
  params = line.split()
  cur = int(params[0])
  line = input()
  other = list(map(int, line.split()))
  other = sorted(other)
  result = findMinimum(cur, other, 0)
  print("Case #" + str(i) + ": " + str(result))

def main():
  line = input()
  if line:
    number = int(line)
    for i in range(number):
      processCase(i + 1)

main()
