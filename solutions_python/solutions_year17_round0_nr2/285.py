def lastTidyNumber(n):
  string = str(n)
  result = 0
  previousDigit = 0
  remainingDigits = len(str(n))
  for digit in map(int, string):
    if digit < previousDigit:
      result = lastTidyNumber(result - 1)
      result *= 10**remainingDigits
      result += 10**remainingDigits - 1
      return result
    else:
      result = result * 10 + digit
      remainingDigits -= 1
      previousDigit = digit
  return result

with open('../inputs/B-large.in') as infile:
  with open('../outputs/B-large.out', 'wb') as outfile:
    cases = int(infile.readline())
    for i in xrange(cases):
      outfile.write('Case #' + str(i + 1) + ': ')
      outfile.write(str(lastTidyNumber(int(infile.readline()))))
      outfile.write('\n')
