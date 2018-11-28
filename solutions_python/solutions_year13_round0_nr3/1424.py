import sys
import math

inp = open(sys.argv[1])
out = open(sys.argv[1].replace(".in",".out"), "w")

def count(case, first, last):
  roots = range(int(math.ceil(math.sqrt(first))), int(math.floor(math.sqrt(last))+1))
  count = 0
  for root in roots:
    if is_pal(root):
      count += 1
  return "Case #%d: %d\n"%(case, count)
  
  
def is_pal(square):
  if str(square) != str(square)[::-1]:
    return False
  arr = map(int, list(str(square)))
  total = 0
  for num in arr:
    total += num**2
  if total < 10:
    return True
  else:
    return False

cases = int(inp.readline().strip())
for i in range(cases):
  num_range = map(int,(inp.readline().strip().split()))
  out.write(count(i+1, num_range[0], num_range[1])) 

  
