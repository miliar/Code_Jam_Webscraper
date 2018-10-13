import sys

def solve(pancakes, size):
  count = 0
  v = []
  for i in pancakes:
    if i == '-':
      v.append(0)
    else:
      v.append(1)

  n = len(pancakes)

  for i in range(0, n - size + 1):
    if v[i] == 0:
      for j in range(i, i + size):
        v[j] = 1 - v[j]
      count += 1

  for i in range(n - size + 1, n):
    if v[i] == 0:
      return "IMPOSSIBLE"

  return count

def main():
  args = sys.argv
  if len(args) == 1:
    print "No input file"
    return

  input = open(args[1], 'r')
  tests = int(input.readline())

  for test in range(tests):
    line = input.readline().split(" ")
    print "Case #%s: %s" % (test + 1, solve(line[0], int(line[1])))

if __name__ == "__main__":
  main()
