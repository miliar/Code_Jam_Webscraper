import sys

def rot(n):
  return n[-1] + n[0:-1]

def how_many_less_than_m(mapping, m):
  result = 0
  for item in mapping:
    if (item <= m):
      result = result + 1
  return result
  
def get_result(A, B, mappings):
  result = 0
  emptyset = set()
  for i in range(A, B):
    mapping = mappings.get(i) or emptyset
    result = result + how_many_less_than_m(mapping, B)
  return result

mappings = {}
for i in range(2000000):
  bigger_recycled_numbers = set()
  stri = str(i)
  iprime = rot(stri)
  while (iprime != stri):
    j = int(iprime)
    if (j > i and j <= 2000000):
      bigger_recycled_numbers.add(j)
    iprime = rot(iprime)
  if (len(bigger_recycled_numbers) > 0):
    mappings[i] = bigger_recycled_numbers

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  AB = [int(v) for v in infile.readline().split()]
  A = AB[0]
  B = AB[1]
  print get_result(A, B, mappings)
  
  
infile.close()