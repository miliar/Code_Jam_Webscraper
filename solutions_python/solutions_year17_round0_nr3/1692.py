import sys
import math

# cosine of two vectors
def calc_num(n, k):
  x = int(math.log(k, 2))
#  print "x", x
  number_curr_layer = k+1 - 2**x
#  print "number_curr_layer", number_curr_layer
  contains_small = False
  last_layer = dict()
  last_layer[n] = 1
  for _ in range(x):
    new_layer = dict()
    max_val = max(last_layer.keys())
    new_layer[max_val//2] = 0
    new_layer[max_val//2 - 1] = 0
    for key in last_layer:
      if (key%2 == 0):
        new_layer[key//2] += last_layer[key]
        new_layer[key//2-1] += last_layer[key]
      else:
        new_layer[key//2] += 2*last_layer[key]
    if new_layer[max_val//2 - 1] == 0:
      del new_layer[max_val//2 - 1]
    last_layer = new_layer
  small, large = (min(last_layer.keys()), max(last_layer.keys()))
#  print small, large
  if number_curr_layer <= last_layer[large]:
    split = large
  else: 
    split = small
  if split % 2 == 0:
    return (split//2, split//2-1)
  else:
    return (split//2, split//2)


#print calc_num(100, 5)
#exit(0)
in_file = open(sys.argv[1])
num = int(in_file.readline().strip())
cnt = 0
for line in in_file:
  n, k = [int(ele) for ele in line.strip().split()]
  res = calc_num(n, k)
  print "Case #"+str(cnt+1)+": " + str(res[0])+" "+str(res[1])
  cnt += 1
  if cnt == num:
    break
in_file.close()
