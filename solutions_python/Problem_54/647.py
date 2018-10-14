import sys

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a
  
def list_gcd(list):
  return_value = list[0]
  for i in range(1, len(list)):
    return_value = gcd(return_value, list[i])
  return return_value

def increment_list(list, step):
  for i in range(len(list)):
    list[i] += step
  
def process_case(values):
  lim = max(values)
  step = list_gcd(values)
  max_seen = 0

  y = 0
  R = 0
  while y < lim:
    x = list_gcd(values)
    if (x > max_seen):
      max_seen = x
      step = x
      R = y
    increment_list(values, step)
    y += step
  return R

filename = sys.argv[1]

infile = open(filename)

C = int(infile.readline())

for x in range(C):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  line = [int(v) for v in infile.readline().split()]
  N = line[0]
  values = line[1:]
  
  print process_case(values)

infile.close()
