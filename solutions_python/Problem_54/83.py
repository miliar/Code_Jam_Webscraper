input = [line.strip("\n") for line in open("input.txt", "r").readlines()]
cases = int(input[0])

def gcd(a, b):
  while (a > 0) and (b > 0):
    if a > b: a = a % b
    else: b = b % a
  return a + b

def solve(data):
  n = int(data[0])
  values = [int(item) for item in data[1:]]
  delta = []
  for i in xrange(1, len(values)):
    delta.append(abs(values[i]-values[i-1]))
  t = reduce(gcd, delta)
  y = values[1] % t
  if y != 0: y = t - y
  print y


for case in xrange(1, cases + 1):
  print "Case #%d:" % case,
  data = input[case].split()
  solve(data)


