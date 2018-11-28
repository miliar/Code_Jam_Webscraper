import sys
args = sys.argv
fname = args[1]
lines = []

def readfile():
  file = open(fname)
  data = file.readlines()
  file.close
  for line in data[1:]:
    lines.append(line.strip().split(" ")[1])
  return lines

def solve_case(idx):
  caseno = idx+1
  S = parse_case(lines[idx])
  required = 0
  standing = 0
  for Si, num in enumerate(S):
    diff = 0
    if (standing < Si):
      diff = Si - standing
    standing += num + diff
    required += diff
  return "Case #{0}: {1}".format(caseno, required)
  
def parse_case(str):
  S = []
  for char in str:
    S.append(int(char))
  return S

def output():
  readfile()
  file = open('answer.txt', 'w')
  for i in xrange(len(lines)):
    data = solve_case(i)
    file.write(data+"\n")
  file.close()
  
output()