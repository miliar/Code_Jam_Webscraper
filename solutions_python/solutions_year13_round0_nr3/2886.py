from math import sqrt

def iter_file_lines(filename):
  with open(filename) as f:
    for line in f:
      line = line.rstrip()
      if len(line):
        yield line

def extract_ints(line):
  return tuple(int(x) for x in line.split())

def is_fair(number):
  if number < 10:
    return True

  s = str(number)
  return s == s[::-1]

def is_square(number):
  return pow(int(sqrt(number)), 2) == number

def is_fair_and_square(number):
  if not is_fair(number):
    return False

  if not is_square(number):
    return False

  return is_fair(int(sqrt(number)))

# assert is_fair_and_square(1)
# assert is_fair_and_square(9)
# assert is_fair_and_square(121)
# assert not is_fair_and_square(16)
# assert not is_fair_and_square(22)
# assert not is_fair_and_square(676)

def fair_and_square_in_range(a, b):
  count = 0
  for j in xrange(n, m + 1):
    if is_fair_and_square(j):
      count += 1
  return count

if __name__ == '__main__':
  lines = iter_file_lines('C-small-attempt0.in')
  testcases = int(lines.next())
  results = []
  for i in range(testcases):
    n, m = extract_ints(lines.next())

    count = fair_and_square_in_range(n, m)

    results.append("Case #%i: %i" % (i + 1, count))

  with open('fair-square-out.txt', 'w') as f:
    for result in results:
      print result
      f.write(result + '\n')
