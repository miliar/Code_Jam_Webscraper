import sys

def solve(number):
  digits = []
  for i in number:
    digits.append(int(i))

  n = len(digits)
  for i in range(n - 1, 0, -1):
    if digits[i] < digits[i - 1]:
      digits[i - 1] -= 1
      for j in range(i, n):
        digits[j] = 9

  ret = 0
  for i in range(0, n):
    ret *= 10
    ret += digits[i]
  return ret

def main():
  args = sys.argv
  if len(args) == 1:
    print "No input file"
    return

  input = open(args[1], 'r')
  tests = int(input.readline())

  for test in range(tests):
    line = input.readline()
    print "Case #%s: %s" % (test + 1, solve(line.strip()))

if __name__ == "__main__":
  main()
