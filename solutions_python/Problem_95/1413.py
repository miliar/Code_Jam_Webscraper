import sys

sample = """3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
""".splitlines()

DEBUG = False

input = []
output = []

num_samples = int(sample[0])

for i in range(num_samples):
  input.append(sample[i + 1])

for i in range(num_samples):
  output.append(sample[i + num_samples + 1].split(': ', 2)[1])

forward = {}
reverse = {}

if DEBUG:
  print input
  print output

for i in range(num_samples):
  for j in range(len(input[i])):
    forward[output[i][j]] = input[i][j]
    reverse[input[i][j]] = output[i][j]

forward['z'] = 'q'
forward['q'] = 'z'
reverse['q'] = 'z'
reverse['z'] = 'q'

if DEBUG:
  print forward
  print reverse
  print len(reverse)

  for c in range(ord('a'), ord('z') + 1):
    if not chr(c) in forward:
      print "not in forward: " + chr(c)
    if not chr(c) in reverse:
      print "not in reverse: " + chr(c)

with sys.stdin as fp:
  num_cases = int(fp.readline())

  for i in range(num_cases):
    line = fp.readline().strip()
    result = ''
    for j in range(len(line)):
      result += reverse[line[j]]
    print "Case #%d: %s" % (i + 1, result)
