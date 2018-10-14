from math import sqrt

def print_ans (id, res):
  print 'Case #%d:'%(id + 1),res

def is_good (val):
  buf  = str(val)
  size = len(buf)
  for i in range(size / 2):
    if buf[i] != buf[size - 1 - i]:
      return False
  buf  = str(val * val)
  size = len(buf)
  for i in range(size / 2):
    if buf[i] != buf[size - 1 - i]:
      return False
  return True

fin = open('data.in')
cases = int(fin.readline())

for case_id in range(cases):
  line = fin.readline()
  data = line.rstrip().split(' ')
  inA  = int((data[0]))
  inB  = int((data[1]))
  A    = int(round(sqrt(inA)))
  B    = int(round(sqrt(inB)))
  if A * A < inA:
    A += 1
  count = 0

  for pos in range(A,B + 1):
    if pos * pos > inB:
      break
    if (is_good(pos)):
      count += 1
  print_ans(case_id, count)

fin.close()